import os
import re
import subprocess
import glob

# Collect md files
md_files = glob.glob("explanations/*.md")

# Collect python scripts
scripts = glob.glob("*.py")
scripts = [s for s in scripts if s not in ("generate_report.py", "add_code_breakdowns.py") and not s.startswith("temp_")]
scripts.sort(key=lambda x: (int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 999, x))

os.makedirs('outputs', exist_ok=True)

for script in scripts:
    print(f"Processing {script}...")
    with open(script, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Patch plt.show()
    image_path = f"outputs/{script.replace('.py', '.png')}"
    code = re.sub(r'plt\.show\(\)', f"plt.savefig('{image_path}')\nplt.close()", code)
    
    temp_script = f"temp_{script}"
    with open(temp_script, 'w', encoding='utf-8') as f:
        f.write(code)
    
    try:
        result = subprocess.run(["python", temp_script], capture_output=True, text=True, timeout=60)
        output = result.stdout.strip()
        error = result.stderr.strip()
        
        new_text = output
        if error:
            new_text += ("\n\nErrors/Warnings:\n" if output else "Errors/Warnings:\n") + error
        if not new_text:
            new_text = "*No output printed to console.*"

        # Escape backslashes for regex replacement
        new_text = new_text.replace('\\', '\\\\')

        # Find markdown file
        if script == '8o.py':
            script_prefix = '8o'
        else:
            script_prefix = re.search(r'^\d+', script).group()
            
        target_md = next((md for md in md_files if os.path.basename(md).startswith(script_prefix + "_")), None)
        
        if target_md:
            with open(target_md, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Split by sections
            sections = re.split(r'(?=### )', content)
            
            for i, section in enumerate(sections):
                if section.startswith(f"### {script}"):
                    # Look for the Output block in this section
                    out_pattern = r'(\*\*Output:\*\*\s*\n```(?:text)?\n).*?(?=\n```)'
                    if re.search(out_pattern, section, re.DOTALL):
                        sections[i] = re.sub(out_pattern, rf'\g<1>{new_text}', section, flags=re.DOTALL)
                        print(f"  -> Updated text output in {target_md}")
                    break
            
            # Join and write back
            with open(target_md, 'w', encoding='utf-8') as f:
                f.write("".join(sections))
                
    except subprocess.TimeoutExpired:
        print(f"Timeout running {script}")
    except Exception as e:
        print(f"Error running {script}: {e}")
    finally:
        if os.path.exists(temp_script):
            try:
                os.remove(temp_script)
            except:
                pass

print("Done updating dynamic outputs.")
