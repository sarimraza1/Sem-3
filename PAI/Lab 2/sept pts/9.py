config = (
    "App",
    "1.6",
    ("Windows", "Linux", "Mac"),
    ("localhost", 3306)
)

print(config)

try:
    config[0] = "NewApp"
except TypeError as e:
    print("cant modify:", e)
