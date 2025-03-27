import os
import shutil
from pathlib import Path

def extract_system_files():
    """Extracts system.md files and renames them to parent folder names"""
    # Set paths relative to script location
    script_dir = Path(__file__).parent
    patterns_dir = script_dir / "patterns"
    output_dir = script_dir / "extracted_patterns"
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    # Process each system.md file
    for root, _, files in os.walk(patterns_dir):
        if "system.md" in files:
            parent_folder = Path(root).name
            source_file = Path(root) / "system.md"
            dest_file = output_dir / f"{parent_folder}.md"
            
            # Copy with overwrite protection
            if dest_file.exists():
                print(f"⚠️  Skipped (exists): {dest_file}")
                continue
                
            shutil.copy2(source_file, dest_file)
            print(f"✓ Copied: {source_file} → {dest_file}")

if __name__ == "__main__":
    print("Starting extraction...\n")
    extract_system_files()
    print("\nExtraction complete!")