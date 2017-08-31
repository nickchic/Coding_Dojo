name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
  new_dict = {}
  for idx in range(len(arr1)):
      new_dict[arr1[idx]] = arr2[idx]
  return new_dict

print make_dict(name,favorite_animal)

name_b = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal_b = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins"]

def make_dict_hacker(arr1, arr2):
    new_dict = {}
    if len(arr1) > len(arr2):
        for idx in range(len(arr1)):
            new_dict[arr1[idx]] = arr2[idx]
        return new_dict
    else:
        for idx in range(len(arr2)):
            new_dict[arr2[idx]] = arr1[idx]
        return new_dict

print make_dict_hacker(name,favorite_animal)
