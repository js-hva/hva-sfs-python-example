from api.amsterdam_api import AmsterdamApi


def main():
    amsterdam_api = AmsterdamApi()
    list_trash_bins = amsterdam_api.get_trash_bins()

    weightTotal = 0
    weightHigh = 0
    weightLow = 0

    print("Overview of trash bins in Amsterdam")

    for trash_bin in list_trash_bins:
        print(
            str(trash_bin['id']) + "\t" +
            trash_bin['name'] + "\t" +
            trash_bin['type'] + "\t" +
            trash_bin['address'] + "\t" +
            str(trash_bin['weight'])
        )
        weightTotal += trash_bin['weight']

        if trash_bin['weight'] >= weightHigh:
            weightHigh = trash_bin['weight']

        #if trash_bin['weight'] =< weightLow:
        #weightLow = min(list_trash_bins)

    print('\nTotal weight is : ' + str(weightTotal))
    print('Mean weight is : ' + str(weightTotal/len(list_trash_bins)))
    print('Highest weight is : ' + str(weightHigh))


if __name__ == "__main__":
    main()
