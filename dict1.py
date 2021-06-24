def main():
    employee={11:{"name":"piyush","age":30},21:{"name":"amar","age":22},51:{"name":"siddi",
        "age":23}}#nested dict

    print("employee information:")
    for eid,einformation in employee.items():#nested loop
        print("employee id",eid)
        for key in einformation:
            print(key,einformation[key])

if __name__=="__main__":
    main()