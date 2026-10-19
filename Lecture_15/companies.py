
import csv

try:
    with open("ssl_companies.csv", "r",  newline="",) as file:
        reader = csv.DictReader(file)

        for row in reader:
            if int(row["Number of employees"]) > 1000:
                print(row)
except:
    print("File did not found.")

import csv

header = ["Name", "Industry", "Number of employees"]
company = [
    {'Organization Id': 'FAB0d41d5b5d22c', 'Name': 'Ferrell LLC', 'Website': 'https://price.net/', 'Industry': 'Plastics', 'Number of employees': '3498'},
    {'Organization Id': '219233e8aFF1BC3', 'Name': 'Hansen-Everett', 'Website': 'https://www.kidd.org/', 'Industry': 'Publishing Industry', 'Number of employees': '7832'},
    {'Organization Id': 'ccc93DCF81a31CD', 'Name': 'Mcintosh-Mora', 'Website': 'https://www.brooks.com/', 'Industry': 'Import / Export', 'Number of employees': '4389'},
    {'Organization Id': 'eb3B7D06cCdD609', 'Name': 'Crane-Clarke', 'Website': 'https://www.sandoval.com/', 'Industry': 'Food / Beverages', 'Number of employees': '9011'},
    {'Organization Id': '8D0c29189C9798B', 'Name': 'Keller, Campos and Black', 'Website': 'https://www.garner.info/', 'Industry': 'Museums / Institutions', 'Number of employees': '2862'},
    {'Organization Id': 'c1Ce9B350BAc66b', 'Name': 'Weiss and Sons', 'Website': 'https://barrett.com/', 'Industry': 'Plastics', 'Number of employees': '5984'},
    {'Organization Id': '7Cb3AeFcE4Ba31e', 'Name': 'Rivas Group', 'Website': 'https://hebert.org/', 'Industry': 'Logistics / Procurement', 'Number of employees': '4155'},
    {'Organization Id': '9E6Acb51e3F9d6F', 'Name': 'Glass, Barrera and Turner', 'Website': 'https://dunlap.com/', 'Industry': 'Utilities', 'Number of employees': '2610'},
    {'Organization Id': '19E3a5Bf6dBDc4F', 'Name': 'Cuevas-Moss', 'Website': 'https://dodson-castaneda.net/', 'Industry': 'Music', 'Number of employees': '9995'},
    {'Organization Id': 'decab0D5027CA6a', 'Name': 'Arroyo Inc', 'Website': 'https://www.turner.com/', 'Industry': 'Writing / Editing', 'Number of employees': '9067'},
    {'Organization Id': 'A2D89Ab9bCcAd4e', 'Name': 'Mitchell, Warren and Schneider', 'Website': 'https://fox.biz/', 'Industry': 'Capital Markets / Hedge Fund / Private Equity', 'Number of employees': '3816'},
    {'Organization Id': '77aDc905434a49f', 'Name': 'Prince PLC', 'Website': 'https://www.watts.com/', 'Industry': 'Individual / Family Services', 'Number of employees': '7645'},
    {'Organization Id': '1eD64cFe986BBbE', 'Name': 'Walton-Barnett', 'Website': 'https://ashley-schaefer.com/', 'Industry': 'Luxury Goods / Jewelry', 'Number of employees': '1746'},
    {'Organization Id': 'CbBbFcdd0eaE2cF', 'Name': 'Bartlett-Arroyo', 'Website': 'https://cruz.com/', 'Industry': 'Civic / Social Organization', 'Number of employees': '3987'},
    {'Organization Id': '7b3fe6e7E72bFa4', 'Name': 'Berg-Sparks', 'Website': 'https://cisneros-love.com/', 'Industry': 'Arts / Crafts', 'Number of employees': '2073'},
    {'Organization Id': '7D9FBF85cdC3871', 'Name': 'Lawson and Sons', 'Website': 'https://www.wong.com/', 'Industry': 'Arts / Crafts', 'Number of employees': '3527'},
    {'Organization Id': '7dd18Fb7cB07b65', 'Name': 'Mcguire, Mcconnell and Olsen', 'Website': 'https://melton-briggs.com/', 'Industry': 'Printing', 'Number of employees': '8445'},
    {'Organization Id': 'EF5B55FadccB8Fe', 'Name': 'Charles-Phillips', 'Website': 'https://bowman.com/', 'Industry': 'Mental Health Care', 'Number of employees': '3450'},
    {'Organization Id': 'f8D4B99e11fAF5D', 'Name': 'Odom Ltd', 'Website': 'https://www.humphrey-hess.com/', 'Industry': 'Management Consulting', 'Number of employees': '1825'},
    {'Organization Id': 'e24D21BFd3bF1E5', 'Name': 'Richard PLC', 'Website': 'https://holden-coleman.net/', 'Industry': 'Broadcast Media', 'Number of employees': '4942'},
    {'Organization Id': 'B9BdfEB6D3Ca44E', 'Name': 'Sampson Ltd', 'Website': 'https://blevins.com/', 'Industry': 'Farming', 'Number of employees': '1418'},
    {'Organization Id': '2a74D6f3D3B268e', 'Name': 'Cherry, Le and Callahan', 'Website': 'https://waller-delacruz.biz/', 'Industry': 'Entertainment / Movie Production', 'Number of employees': '7202'},
    {'Organization Id': 'Bf3F3f62c8aBC33', 'Name': 'Cherry PLC', 'Website': 'https://www.avila.info/', 'Industry': 'Plastics', 'Number of employees': '8245'},
    {'Organization Id': 'aeBe26B80a7a23c', 'Name': 'Melton-Nichols', 'Website': 'https://kennedy.com/', 'Industry': 'Legislative Office', 'Number of employees': '8741'},
    {'Organization Id': 'EB9f456e8b7022a', 'Name': 'Soto Group', 'Website': 'https://norris.info/', 'Industry': 'Business Supplies / Equipment', 'Number of employees': '9097'},
    {'Organization Id': 'Dfef38C51D8DAe3', 'Name': 'Poole, Cruz and Whitney', 'Website': 'https://reed.info/', 'Industry': 'Marketing / Advertising / Sales', 'Number of employees': '2992'},
    {'Organization Id': 'cBfe4dbAE1699da', 'Name': 'Erickson, Andrews and Bailey', 'Website': 'https://www.hobbs-grant.com/', 'Industry': 'Consumer Electronics', 'Number of employees': '7829'},
    {'Organization Id': 'ce57DCbcFD6d618', 'Name': 'Newman-Galloway', 'Website': 'https://www.scott.com/', 'Industry': 'Information Technology / IT', 'Number of employees': '3934'},
    {'Organization Id': '5aaD187dc929371', 'Name': 'Frazier-Butler', 'Website': 'https://www.daugherty-farley.info/', 'Industry': 'Outsourcing / Offshoring', 'Number of employees': '5130'},
    {'Organization Id': '32BB9Ff4d939788', 'Name': 'Duffy-Levy', 'Website': 'https://www.potter.com/', 'Industry': 'Wireless', 'Number of employees': '6146'},
    {'Organization Id': 'adcB0afbE58bAe3', 'Name': 'Wagner LLC', 'Website': 'https://decker-esparza.com/', 'Industry': 'International Affairs', 'Number of employees': '6874'},
    {'Organization Id': '208044AC2fe52F3', 'Name': 'Massey LLC', 'Website': 'https://frazier.biz/', 'Industry': 'Accounting', 'Number of employees': '5004'},
    {'Organization Id': 'DDB19Be7eeB56B4', 'Name': 'Cummings-Rojas', 'Website': 'https://simon-pearson.com/', 'Industry': 'Financial Services', 'Number of employees': '7529'},
    {'Organization Id': 'cBa7EFe5D05Adaf', 'Name': 'Crawford-Rivera', 'Website': 'https://black-ramirez.org/', 'Industry': 'Online Publishing', 'Number of employees': '7805'},
    {'Organization Id': 'Ea3f6D52Ec73563', 'Name': 'Montes-Hensley', 'Website': 'https://krueger.org/', 'Industry': 'Printing', 'Number of employees': '8433'},
    {'Organization Id': 'bC0CEd48A8000E0', 'Name': 'Velazquez-Odom', 'Website': 'https://stokes.com/', 'Industry': 'Alternative Dispute Resolution', 'Number of employees': '4044'},
    {'Organization Id': 'c89b9b59BC4baa1', 'Name': 'Eaton-Morales', 'Website': 'https://www.reeves-graham.com/', 'Industry': 'Capital Markets / Hedge Fund / Private Equity', 'Number of employees': '7013'},
    {'Organization Id': 'e0E8e27eAc9CAd5', 'Name': 'George, Russo and Guerra', 'Website': 'https://drake.com/', 'Industry': 'Military Industry', 'Number of employees': '2880'},
    {'Organization Id': 'B97a6CF9bf5983C', 'Name': 'Davila Inc', 'Website': 'https://mcconnell.info/', 'Industry': 'Consumer Electronics', 'Number of employees': '2215'},
    {'Organization Id': '8cC1bDa330a5871', 'Name': 'Pineda-Morton', 'Website': 'https://www.carr.com/', 'Industry': 'Printing', 'Number of employees': '6168'},
    {'Organization Id': 'ED889CB2FE9cbd3', 'Name': 'Huang and Sons', 'Website': 'https://www.bolton.com/', 'Industry': 'Semiconductors', 'Number of employees': '7484'},
    {'Organization Id': 'F4Dc1417BC6cb8f', 'Name': 'Gilbert-Simon', 'Website': 'https://www.bradford.biz/', 'Industry': 'Newspapers / Journalism', 'Number of employees': '1927'},
    {'Organization Id': 'dEbDAAeDfaed00A', 'Name': 'Rowe and Sons', 'Website': 'https://www.simpson.org/', 'Industry': 'Facilities Services', 'Number of employees': '8172'},
    {'Organization Id': '61BDeCfeFD0cEF5', 'Name': 'Valenzuela, Holmes and Rowland', 'Website': 'https://www.dorsey.net/', 'Industry': 'Transportation', 'Number of employees': '1483'},
    {'Organization Id': '4e91eD25f486110', 'Name': 'Best, Wade and Shepard', 'Website': 'https://zimmerman.com/', 'Industry': 'Gambling / Casinos', 'Number of employees': '4873'},
    {'Organization Id': '0a0bfFbBbB8eC7c', 'Name': 'Holmes Group', 'Website': 'https://mcdowell.org/', 'Industry': 'Photography', 'Number of employees': '2988'},
]


with open("sorted_companies.csv", "w",  newline="",) as new_file:
    writer = csv.DictWriter(new_file,fieldnames=header,extrasaction="ignore")

    writer.writeheader()
    writer.writerows(company)

   