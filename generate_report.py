import os
import re
import subprocess
import glob

# Collect all Python files except this one
scripts = glob.glob("*.py")
scripts = [s for s in scripts if s not in ("generate_report.py", "runner.py") and not s.startswith("temp_")]
# Sort numerically and alphabetically
scripts.sort(key=lambda x: (int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 999, x))

os.makedirs('outputs', exist_ok=True)
md_content = "# Machine Learning Lab Explanations\n\n"

for script in scripts:
    print(f"Processing {script}...")
    with open(script, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Patch plt.show()
    image_path = f"outputs/{script.replace('.py', '.png')}"
    
    # Replace all variations of plt.show()
    code = re.sub(r'plt\.show\(\)', f"plt.savefig('{image_path}')\nplt.close()", code)
    
    # Write to a temp file
    temp_script = f"temp_{script}"
    with open(temp_script, 'w', encoding='utf-8') as f:
        f.write(code)
    
    try:
        # We need to set the working directory to the same one as the original scripts
        result = subprocess.run(["python", temp_script], capture_output=True, text=True, timeout=60)
        output = result.stdout
        error = result.stderr
        
        md_content += f"## `{script}`\n\n"
        if output.strip() or error.strip():
            md_content += "### Output\n"
            if output.strip():
                md_content += f"```text\n{output.strip()}\n```\n\n"
            if error.strip():
                md_content += f"**Errors/Warnings:**\n```text\n{error.strip()}\n```\n\n"
        else:
            md_content += "### Output\n*No output printed to console.*\n\n"
        
        # Check if plot was generated
        if os.path.exists(image_path):
            md_content += "### Graph\n"
            # Adjust path to be relative for markdown
            rel_image_path = image_path.replace('\\', '/')
            md_content += f"![{script}]({rel_image_path})\n\n"
            
    except subprocess.TimeoutExpired:
        md_content += f"## `{script}`\n\nFailed to run {script}: Execution timed out after 60 seconds\n\n"
    except Exception as e:
        md_content += f"## `{script}`\n\nFailed to run {script}: {str(e)}\n\n"
        
    finally:
        if os.path.exists(temp_script):
            try:
                os.remove(temp_script)
            except:
                pass

with open('explanation.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

print("Done generating explanation.md")
