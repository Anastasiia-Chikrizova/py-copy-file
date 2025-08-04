def copy_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "cp":
        return  

    src, dst = parts[1], parts[2]

    if src == dst:
        return  
        
    with open(src, "r", encoding="utf-8") as file_in, open(dst, "w", encoding="utf-8") as file_out:
        file_out.write(file_in.read())
