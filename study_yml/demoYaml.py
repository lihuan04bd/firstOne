import yaml
file = open("data.yaml",encoding="utf-8")
result = yaml.load(file,Loader= yaml.FullLoader)
print(result)
print(type(result))
print(type(result))
