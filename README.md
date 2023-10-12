# InfilectTest
**This is Fast API project**

1. Clone this repo from this github link https://github.com/MadhuryaReddy31/InfilectTest.git
2. open the project in VS code or pycharm. 
3. In terminal, run the below command to build docker image
**docker build -t infilect .**
4. run the docker using the below command
**docker run -p 8000:8000 infilect**
5. Once you see Application startup complete access your API's in swagger using this link **http://localhost:8000/docs**
6. Now you can test the API's
7. our main API is /shelf_identification
8. *test case 1:*
[
    ["G", "G", "M", "M"],
    ["G", "G", "M", "M"],
    ["B", "B", "N", "N"],
    ["B", "B", "N", "N"]
]


*test case:2*
[
        ["G", "M", "N", "B"],
        ["G", "M", "N", "B"],
        ["G", "M", "N", "B"],
        ["G", "M", "N", "B"]
]


*test case:3*
[
    ["G", "G", "G", "M", "M", "M", "M"],
    ["G", "B", "G", "M", "N", "N", "M"],
    ["G", "G", "G", "M", "N", "N", "M"],
    ["B", "B", "B", "B", "B", "N", "N"]
]

