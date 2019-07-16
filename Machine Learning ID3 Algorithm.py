from math import *


def split_age_lists(dataset, val):
    table = []
    for i in dataset:
        if i.age == val:
           table.append(i)
    return table


def split_pres_lists(dataset, val):
    table = []
    for i in dataset:
        if i.prescription == val:
            table.append(i)
    return table


def split_ast_lists(dataset, val):
    table = []
    for i in dataset:
        if i.astigmatic == val:
            table.append(i)
    return table


def split_tear_lists(dataset, val):
    table = []
    for i in dataset:
        if i.tearRate == val:
            table.append(i)
    return table


def cacl_label_for_Age(dataset):
    idx = -1
    pos_1 = 0  # need license with value age 1
    neg_1 = 0  # don't need license with value age 1
    pos_0 = 0  # need license with value age 0
    neg_0 = 0  # don't need license with value age 0
    for i in dataset:
        if i.age == 0:
            if i.needLense == 0:
                neg_0 += 1
            elif i.needLense == 1:
                pos_0 += 1
        elif i.age == 1:
            if i.needLense == 0:
                neg_1 += 1
            elif i.needLense == 1:
                pos_1 += 1
    return pos_1, neg_1, pos_0, neg_0


def calc_label_for_prescription(dataset):
    idx = -1
    pos_1 = 0  # need license with value age 1
    neg_1 = 0  # don't need license with value age 1
    pos_0 = 0  # need license with value age 0
    neg_0 = 0  # don't need license with value age 0
    for i in dataset:
        if i.prescription == 0:
            if i.needLense == 0:
                neg_0 += 1
            elif i.needLense == 1:
                pos_0 += 1
        elif i.prescription == 1:
            if i.needLense == 0:
                neg_1 += 1
            elif i.needLense == 1:
                pos_1 += 1
    return pos_1, neg_1, pos_0, neg_0


def calc_label_for_astigmatic(dataset):
    idx = -1
    pos_1 = 0  # need license with value age 1
    neg_1 = 0  # don't need license with value age 1
    pos_0 = 0  # need license with value age 0
    neg_0 = 0  # don't need license with value age 0
    for i in dataset:
        if i.astigmatic == 0:
            if i.needLense == 0:
                neg_0 += 1
            elif i.needLense == 1:
                pos_0 += 1
        elif i.astigmatic == 1:
            if i.needLense == 0:
                neg_1 += 1
            elif i.needLense == 1:
                pos_1 += 1
    return pos_1, neg_1, pos_0, neg_0


def calc_label_for_tearRate(dataset):
    idx = -1
    pos_1 = 0  # need license with value age 1
    neg_1 = 0  # don't need license with value age 1
    pos_0 = 0  # need license with value age 0
    neg_0 = 0  # don't need license with value age 0
    for i in dataset:
        if i.tearRate == 0:
            if i.needLense == 0:
                neg_0 += 1
            elif i.needLense == 1:
                pos_0 += 1
        elif i.tearRate == 1:
            if i.needLense == 0:
                neg_1 += 1
            elif i.needLense == 1:
                pos_1 += 1
    return pos_1, neg_1, pos_0, neg_0


def calc_information(dataset):
    pos = 0
    neg = 0
    t = dataset.__len__()
    for i in dataset:
        if i.needLense == 0:
            neg += 1
        elif i.needLense == 1:
            pos += 1
    return pos, neg, t


def calc_average(total_count, pos_0, neg_0, pos_1, neg_1, e_0, e_1):
    info_average = 1
    info_average = (((pos_0+neg_0)/total_count)*e_0) + (((pos_1+neg_1)/total_count)*e_1)
    return info_average


def Entropy(postives, negatves, total_count):
    if postives == 0 or negatves == 0:
        e = 0
    else:
        e = ((-postives/total_count)*log2(postives/total_count))+((-negatves/total_count)*log2(negatves/total_count))
    return e


class item:
    def __init__(self, age, prescription, astigmatic, tearRate, needLense):
        self.age = age
        self.prescription = prescription
        self.astigmatic = astigmatic
        self.tearRate = tearRate
        self.needLense = needLense


def getDataset():
    data = []
    labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
    data.append(item(0, 0, 0, 0, labels[0]))
    data.append(item(0, 0, 0, 1, labels[1]))
    data.append(item(0, 0, 1, 0, labels[2]))
    data.append(item(0, 0, 1, 1, labels[3]))
    data.append(item(0, 1, 0, 0, labels[4]))
    data.append(item(0, 1, 0, 1, labels[5]))
    data.append(item(0, 1, 1, 0, labels[6]))
    data.append(item(0, 1, 1, 1, labels[7]))
    data.append(item(1, 0, 0, 0, labels[8]))
    data.append(item(1, 0, 0, 1, labels[9]))
    data.append(item(1, 0, 1, 0, labels[10]))
    data.append(item(1, 0, 1, 1, labels[11]))
    data.append(item(1, 1, 0, 0, labels[12]))
    data.append(item(1, 1, 0, 1, labels[13]))
    data.append(item(1, 1, 1, 0, labels[14]))
    data.append(item(1, 1, 1, 1, labels[15]))
    data.append(item(1, 0, 0, 0, labels[16]))
    data.append(item(1, 0, 0, 1, labels[17]))
    data.append(item(1, 0, 1, 0, labels[18]))
    data.append(item(1, 0, 1, 1, labels[19]))
    data.append(item(1, 1, 0, 0, labels[20]))
    return data


class Feature:
    def __init__(self, name):
        self.name = name
        self.visited = -1
        self.infoGain = -1


class ID3:
    def __init__(self, features):
        self.features = features

    def classify(self, input, dataset):
        current_Gain = -99999
        maximum_gain_column_idx = -1
        # takes an array for the features ex. [0, 0, 1, 1]
        # should return 0 or 1 based on the classification
        postives, negatives, total_count = calc_information(dataset)
        Entropy_Label = Entropy(postives, negatives, total_count)

        # this is for age Column
        if self.features[0].visited == -1:
            pos_1_age, neg_1_age, pos_0_age, neg_0_age = cacl_label_for_Age(dataset)

            Entropy_1_age = Entropy(pos_1_age, neg_1_age, pos_1_age+neg_1_age)
            Entropy_0_age = Entropy(pos_0_age, neg_0_age, neg_0_age+pos_0_age)

            average_information_age = calc_average(total_count, pos_0_age, neg_0_age, pos_1_age, neg_1_age,
                                                   Entropy_0_age, Entropy_1_age)

            self.features[0].infoGain = Entropy_Label - average_information_age
            if current_Gain < 0 or self.features[0].infoGain > current_Gain:
                current_Gain = self.features[0].infoGain
                maximum_gain_column_idx = 0

        # this is for prescription Column
        if self.features[1].visited == -1:
            pos_1_pres, neg_1_pres, pos_0_pres, neg_0_pres = calc_label_for_prescription(dataset)

            Entropy_1_pres = Entropy(pos_1_pres, neg_1_pres, pos_1_pres + neg_1_pres)
            Entropy_0_pres = Entropy(pos_0_pres, neg_0_pres, neg_0_pres + pos_0_pres)

            average_information_pres = calc_average(total_count, pos_0_pres, neg_0_pres, pos_1_pres, neg_1_pres,
                                                   Entropy_0_pres, Entropy_1_pres)

            self.features[1].infoGain = Entropy_Label - average_information_pres
            if current_Gain < 0 or self.features[1].infoGain > current_Gain:
                current_Gain = self.features[1].infoGain
                maximum_gain_column_idx = 1

        # this for astigmatic Column
        if self.features[2].visited == -1:
            pos_1_ast, neg_1_ast, pos_0_ast, neg_0_ast = calc_label_for_astigmatic(dataset)

            Entropy_1_ast = Entropy(pos_1_ast, neg_1_ast, pos_1_ast + neg_1_ast)
            Entropy_0_ast = Entropy(pos_0_ast, neg_0_ast, neg_0_ast + pos_0_ast)

            average_information_ast = calc_average(total_count, pos_0_ast, neg_0_ast, pos_1_ast, neg_1_ast,
                                                   Entropy_0_ast, Entropy_1_ast)

            self.features[2].infoGain = Entropy_Label - average_information_ast
            if current_Gain < 0 or self.features[2].infoGain > current_Gain:
                current_Gain = self.features[2].infoGain
                maximum_gain_column_idx = 2

        # this is for tearRate Column
        if self.features[3].visited == -1:
            pos_1_tear, neg_1_tear, pos_0_tear, neg_0_tear = calc_label_for_tearRate(dataset)

            Entropy_1_tear = Entropy(pos_1_tear, neg_1_tear, pos_1_tear + neg_1_tear)
            Entropy_0_tear = Entropy(pos_0_tear, neg_0_tear, neg_0_tear + pos_0_tear)

            average_information_tear = calc_average(total_count, pos_0_tear, neg_0_tear, pos_1_tear, neg_1_tear,
                                                    Entropy_0_tear, Entropy_1_tear)

            self.features[3].infoGain = Entropy_Label - average_information_tear
            if current_Gain < 0 or self.features[3].infoGain > current_Gain:
                current_Gain = self.features[3].infoGain
                maximum_gain_column_idx = 3

        self.features[maximum_gain_column_idx].visited = 1
        if maximum_gain_column_idx == 0:
            if Entropy_0_age == 0:
                if pos_0_age != 0 and input[0] == 0:
                    return 1
                elif neg_0_age != 0 and input[0] == 0:
                    return 0
            if Entropy_1_age == 0:
                if pos_1_age != 0 and input[0] == 1:
                    return 1
                elif neg_1_age != 0 and input[0] == 1:
                    return 0

            if Entropy_0_age != 0:
                table_0 = split_age_lists(dataset, 0)
                return self.classify(input, table_0)
            if Entropy_1_age != 0:
                table_0 = split_age_lists(dataset, 1)
                return self.classify(input, table_0)

        elif maximum_gain_column_idx == 1:
            if Entropy_0_pres == 0:
                if pos_0_pres != 0 and input[1] == 0:
                    return 1
                elif neg_0_pres != 0 and input[1] == 0:
                    return 0
            if Entropy_1_pres == 0:
                if pos_1_pres != 0 and input[1] == 1:
                    return 1
                elif neg_1_pres != 0 and input[1] == 1:
                    return 0

            if Entropy_0_pres != 0:
                table_0 = split_age_lists(dataset, 0)
                return self.classify(input, table_0)
            if Entropy_1_pres != 0:
                table_0 = split_pres_lists(dataset, 1)
                return self.classify(input, table_0)

        elif maximum_gain_column_idx == 2:
            if Entropy_0_ast == 0:
                if pos_0_ast != 0 and input[2] == 0:
                    return 1
                elif neg_0_ast != 0 and input[2] == 0:
                    return 0
            if Entropy_1_ast == 0:
                if pos_1_ast != 0 and input[2] == 1:
                    return 1
                elif neg_1_ast != 0 and input[2] == 1:
                    return 0

            if Entropy_0_ast != 0:
               table_0 = split_age_lists(dataset, 0)
               return  self.classify(input, table_0)
            if Entropy_1_ast != 0:
                table_0 = split_ast_lists(dataset, 1)
                return self.classify(input, table_0)

        elif maximum_gain_column_idx == 3:
            if Entropy_0_tear == 0:
                if pos_0_tear != 0 and input[3] == 0:
                    return 1
                elif neg_0_tear != 0 and input[3] == 0:
                    return 0
            if Entropy_1_tear == 0:
                if pos_1_tear != 0 and input[3] == 1:
                    return 1
                elif neg_1_tear != 0 and input[3] == 1:
                    return 0

            if Entropy_0_tear != 0:
                table_0 = split_tear_lists(dataset, 0)
                return  self.classify(input, table_0)
            if Entropy_1_tear != 0:
                table_0 = split_tear_lists(dataset, 1)
                return self.classify(input, table_0)




dataset = getDataset()
features = [Feature('age'), Feature('prescription'), Feature('astigmatic'), Feature('tearRate')]
id3 = ID3(features)
cls = id3.classify([0, 0, 1, 1], dataset)  # should print 1
print('testcase 1: ', cls)

features = [Feature('age'), Feature('prescription'), Feature('astigmatic'), Feature('tearRate')]
id3 = ID3(features)
cls = id3.classify([1, 1, 0, 0], dataset)  # should print 0
print('testcase 2: ', cls)

features = [Feature('age'), Feature('prescription'), Feature('astigmatic'), Feature('tearRate')]
id3 = ID3(features)
cls = id3.classify([1, 1, 1, 0], dataset)  # should print 0
print('testcase 3: ', cls)

features = [Feature('age'), Feature('prescription'), Feature('astigmatic'), Feature('tearRate')]
id3 = ID3(features)
cls = id3.classify([1, 1, 0, 1], dataset)  # should print 1
print('testcase 4: ', cls)






