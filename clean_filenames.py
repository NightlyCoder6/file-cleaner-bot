import os


def clean_filenames(folder_path):
    fixed_ext = {'.jpeg': '.jpg', '.htm': '.html'}

    for filename in os.listdir(folder_path):
        old_path = os.path.join(folder_path, filename)

        if os.path.isfile(old_path):
            name, ext = os.path.splitext(filename)
            clean_name = name.strip().lower().replace(' ', '_')
            ext = ext.lower()
            ext = fixed_ext.get(ext, ext)

            new_filename = clean_name + ext
            new_path = os.path.join(folder_path, new_filename)

            if new_path != old_path and not os.path.exists(new_path):
                os.rename(old_path, new_path)
                print(f'Renamed: {filename} → {new_filename}')
            else:
                print(f'Skipped: {filename}')


if __name__ == "__main__":
    folder = input("Enter the folder path to clean: ").strip().strip('"').strip("'")

    if os.path.isdir(folder):
        clean_filenames(folder)
    else:
        print("❌ Invalid folder path.")
