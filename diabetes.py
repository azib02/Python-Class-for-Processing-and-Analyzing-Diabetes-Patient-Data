"""
@author: azib

"""
import csv


class Diabetes:
    def __init__(self, filepath) -> None:
        # Try to open the CSV file
        try:
            with open(filepath, 'r') as csvfile:
                reader = csv.reader(csvfile)
                self.header = next(reader)
                self.data = list(reader)
        # raise eception error, if the file doesn't exist
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{filepath }' is not found.")

    def get_dimension(self) -> list:
        return [len(self.data), len(self.header)]

    def web_summary(self, filepath: str) -> None:
        with open(filepath, 'w') as html:
            html.write("<html>")
            # head of the html file with most of the styling
            html.write("<head>")
            html.write("<meta charset=\"UTF-8\">\n")
            html.write("<style>\n")
            html.write("table {\n")
            html.write("width:550px;\n")
            html.write("font-family: monospace;\n")
            html.write("border-collapse: seperate;\n")
            html.write("border-spacing: 0;\n")
            html.write("margin:0 auto;\n")
            html.write("}\n")
            html.write("th, td {\n")
            html.write("padding: 20px;\n")
            html.write("text-align: center;\n")
            html.write("font-weight:bold;\n")
            html.write("border:3px solid white;\n")
            html.write("}\n")
            html.write("th {\n")
            html.write("background-color:#D8D8D8;\n")
            html.write("border:3px solid white;\n")
            html.write("color:black;\n")
            html.write("}\n")
            html.write("</style>\n")
            html.write("<title>Diabetes Data Summary</title>")
            html.write("<p style=\"font-weight:bold; text-align:center;font-size:26px;\">Diabetes Data Summary</p>")
            html.write("<head>")
            # body of the html code, with table header first row
            html.write("<body>")
            html.write("<table>")
            html.write("<tr>")
            html.write("<th rowspan=6 >ATTRIBUTES</th>")
            html.write("<th style=\"font-weight:bold;\" colspan=6>CLASS</th>")
            html.write("<tr>")
            # second row of the header
            html.write("<tr>")
            html.write("<th colspan=2.5>POSITIVE</th>")
            html.write("<th colspan=2.5>NEGATIVE</th>")
            html.write("<tr>")
            # third and last row of the header
            html.write("<tr>")
            html.write("<th colspan=1.5>YES</th>")
            html.write("<th colspan=0>NO</th>")
            html.write("<th colspan=0>YES</th>")
            html.write("<th colspan=0>NO</th>")
            html.write("<tr>")

            instancesToAvoid = ["class", "gender", "age"]
            # iterate through attributes except the ones in the list
            # can also use for elm in self.header[2:len(self.header)-1]
            # that iterates from third row to second last
            # avoiding therefore age gender and class
            # however, age, class, gender might be in the middle
            # of the table, so more effective avoidInstances
            for elm in self.header:
                if not elm.lower() in instancesToAvoid:
                    # counters for yes/no values for each class
                    positive_yes = 0
                    positive_no = 0
                    negative_yes = 0
                    negative_no = 0
                    # iterate for each row in data and count yes/no values
                    # excluding the header
                    for row in self.data:
                        classValue = row[-1].lower()
                        yesNoChecker = row[self.header.index(elm)].lower()

                        if classValue == 'positive':
                            if yesNoChecker == 'yes':
                                positive_yes += 1
                            else:
                                positive_no += 1

                        elif classValue == 'negative':
                            if yesNoChecker == 'yes':
                                negative_yes += 1
                            else:
                                negative_no += 1
                    # creating rows for each row in data and cells
                    # for yes/no value for each row
                    html.write("<tr>\n")
                    html.write("<td style=\"background-color:#D8D8D8;text-transform:uppercase;text-align:left;\">" + elm + "</td>\n")
                    html.write(f"<td style=\"background-color:#c9fec9;\"> {positive_yes} </td>\n")
                    html.write(f"<td style=\"background-color:ffbeab;\"> {positive_no} </td>\n")
                    html.write(f"<td style=\"background-color:#c9fec9;\"> {negative_yes} </td>\n")
                    html.write(f"<td style=\"background-color:ffbeab;\"> {negative_no} </td>\n")
                    html.write("<tr>\n")
            # closing all opened tags
            html.write("</table>")
            html.write("</body>")
            html.write("</html>")

    def count_instances(self, criteria) -> int:
        """
        Count the number of instances in the data
        set where the specified attributes
        have the specified values
        ----------
        criteria : DICTIONARY

        criteria = { 'Gender':'female' },
        YOU NEED TO MAKE SURE THAT THE FIRST PART,
        THE ATTRIBUTES MATCH THE STYLING IN THE DATA,
        FOR EXAMPLE IF IN THE DATA
        YOU HAVE Gender, WITH UPPERCASE G,
        MAKE SURE TO PUT THE CAPITAL G IN THE
        DICTIONARY AS WELL,
        SAME THING FOR THE VALUE OF THAT ATTRIBUTE,
        IF YOU CHECKING MALE, AND IN THE
        DATA YOU HAVE male,
        ALL LOWERCASE, MAKE SURE TO PUT
        ALL LOWERCASE IN THE
        DICTIONARY AS WELL,ALSO LOOK FOR
        ANY SPELLING MISTAKES,
        YOU NEED TO MATCH THE ATTRIBUTE AND
        VALUE WITH THE STYILING AND SPELLING IN DATA.
        THIS CODE IS CASE SENSITIVE.
        THE FORMAT ON HOW TO WRITE IS:

        name of the dictionary = {'attribute':'value', 'attribute2':'value2',}
        make sure to not use one attribute
        multiple times in the some dictionary:
        can't do: {'gender':'male', 'gender':'female'}
        you can use one attribute only once
        in one dictionary, for value it does not matter, you can repeat.
        to use the function
        treat as a normal function:
            d1 = Diabetes("diabetes_data.csv")
            criteria1 = { 'Gender':'female' }
            d1.count_instances(criteria1)

        Returns
        -------
        int
            WILL RETURN THE COUNT OF HOW MANY TIMES
            THE ATTRIBUTES CHOSEN WITH THE SPECIFIED VALUES
            ARE FOUND IN THE DATA SET.
        """

        if not isinstance(criteria, dict):
            raise ValueError("Invalid input.Expected a dictionary")
        if not all(key in self.header for key in criteria):
            raise ValueError("Invalid attributes,check case correspondance and spelling")

        listFinal = []
        listNew = []

        # iterating to create a list of sublists
        # containing the values of the instances we
        # need
        for elm in self.header:
            if elm.lower() in map(str.lower, criteria):
                for row in self.data:
                    listNew.append(row[self.header.index(elm)].lower())
                listFinal.append(listNew)
                listNew = []
        # ordering my values in the same order
        # of the header for next comparison
        valueCritera = [criteria[elm]for elm in self.header if elm in criteria]
        # creating new sublists with element
        # in the same indeces position in the previous
        # sublist
        transposed_list = list(map(list, zip(*listFinal)))
        # counting how many times the list of instance
        # values appears in the sublists of the transposed
        # list
        countInstances = transposed_list.count(valueCritera)

        return (countInstances)


if __name__ == "__main__":
    # You can comment the following when you are testing your code
    # You can add more tests as you want

    # test diabetes_data.csv
    d1 = Diabetes("diabetes_data.csv")
    print(d1.get_dimension())
    d1.web_summary('stat01.html')
    # d1.count_instances() # change according to your criteria
    # print()
    criteria1 = {'class': 'negative', 'Genital thrush': 'yes'}
    d1.count_instances(criteria1)
    print(d1.count_instances(criteria1))

    # test diabetes2_data.csv
    d2 = Diabetes("diabetes2_data.csv")
    print(d2.get_dimension())
    d2.web_summary('stat02.html')
    # d2.count_instances()  # change according to your criteria
    criteria2 = {'class': 'positive', 'Genital thrush': 'yes'}
    d2.count_instances(criteria2)
    print(d2.count_instances(criteria2))

    d3 = Diabetes("diabetes3_data.csv")
    print(d3.get_dimension())
    d3.web_summary('stat03.html')
    # d2.count_instances()  # change according to your criteria
    criteria3 = {'class': 'negative', 'Obesity': 'no'}
    d3.count_instances(criteria3)
    print(d3.count_instances(criteria3))