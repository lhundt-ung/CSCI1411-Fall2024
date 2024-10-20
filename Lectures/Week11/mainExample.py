def fun1():
    print("Having fun with functions in Python")


#Main function, simplifies long scripts with lots of functions 
def main():
    print("Has main() in script")
    fun1()

#statements below required to have main executed when script is ran
if __name__ == "__main__":
    main()
