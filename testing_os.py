# import os


# def c():
# 	print("################")
# 	dir_path = os.path.dirname(os.path.realpath(__file__))
# 	print("DIRPATH:", dir_path)

# 	cwd = os.getcwd()
# 	print("PWD:", cwd)
# 	print("################")

# c()

# #files = os.listdir(".")
# #os.chdir("Music")

# print(os.listdir("Music"))

# os.chdir("Music")

# c()

# os.chdir("..")
# c()

################
#mutagennnnnnn##
# import music
# import mutagen.ogg
# metadata = mutagen.ogg.Open("Music\\Destroy Boys - Secrets.ogg")
# print(metadata)
import mutagen
s = "Music\Kendrick Lamar - Not Like Us.ogg"
aa = mutagen.File(s)
print(aa["lyrics-xxx"][0])