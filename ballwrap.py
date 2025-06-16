import math
import glob, re

def generate_coords(Dc, Ds, H):
    N = int(round(math.pi * (Dc + Ds) / Ds))
    rows = max(1, int(math.floor(H / Ds)))
    R = (Dc + Ds) / 2

    coords = []
    for i in range(rows):
        for j in range(N):
            phi = j * 2 * math.pi / N + (i % 2) * (math.pi / N)
            x = R * math.cos(phi)
            y = R * math.sin(phi)
            z = Ds/2 + i*Ds
            coords.append((x, y, z))
    return coords

def get_default_filename():
    files = glob.glob("coords*.txt")
    nums = [int(m.group(1)) for f in files if (m:=re.match(r"coords(\d+)\.txt$", f))]
    return f"coords{max(nums)+1 if nums else 1}.txt"

if __name__ == "__main__":
    Dc = float(input("Internal cylinder diameter (Dc): "))
    Ds = float(input("Sphere diameter (Ds): "))
    H  = float(input("Cylinder height (H): "))
    name = input("Output filename (leave blank for default): ").strip()
    filename = name+".txt" if name and not name.endswith(".txt") else (name or get_default_filename())

    coords = generate_coords(Dc, Ds, H)
    if coords:
        x,y,z = coords[0]
        print(f"First ball coordinate: {x:.6f} \t{y:.6f} \t{z:.6f}")
    with open(filename, "w") as f:
        for x,y,z in coords:
            f.write(f"{x:.6f} \t{y:.6f} \t{z:.6f} \t\n")
    print(f"Generated {len(coords)} coordinates and saved to {filename}")
