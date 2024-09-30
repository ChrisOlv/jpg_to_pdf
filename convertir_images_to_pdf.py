import glob, PIL.Image
L = [PIL.Image.open(f) for f in glob.glob('*.jpg')]
L[0].save('out.pdf', "PDF" ,resolution=100.0, save_all=True, append_images=L[1:])