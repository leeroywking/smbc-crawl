from output import listy


def listify_downloads():
    length = len(listy)
    print(length)

    print(listy[0])
    print(listy[length - 1])

    with open("list_of_images.txt", "a") as file1:
        for item in listy:
            file1.write(item["image_url"])
            file1.write("\n")

