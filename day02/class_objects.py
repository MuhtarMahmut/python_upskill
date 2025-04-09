"""
in Java:

class Item{

    String itemName;
    double itemPrice;

    static String madeIn = "China"

    Item(String itemName, double itemPrice){
        this.itemName = itemName;
        this.itemPrice = itemPrice;
    }

}

"""


class Item:
    made_in = 'China'  # static variable
    tariffs = "100%"  # static variable

    def __init__(self, item_name, item_price):
        self.item_name = item_name  # instance variable
        self.item_price = item_price  # instance variable

    def __str__(self):  # instance method
        return f'{type(self).__name__} {self.__dict__}'

    def instance_method(self):
        print("This is an instance method")

    @staticmethod  # can not interact with any instance or static variables
    def static_method():
        print(f"This is a static method")

    @classmethod  # equivilent to static method of java: only accept static variables
    def class_method(cls):
        print(f"This is a class method: {cls.made_in}")


item1 = Item("Pen", 2)
item2 = Item("Book", 4)

print(item1)
print(item2)

print(Item.made_in)
print(Item.tariffs)

Item.class_method()
Item.static_method()


"""
Create Employee class:
    instance variables: employee_name, job_title, salary
    static_variables: pay_tax
    
    instance methods: 
        __init()__: declares and initalizes all the isnace variables
        __str()__: creates string version of the object
        work(): displaye  ${employee_name} is working
        
    class method:
        display_employee_tax_rate()
    

"""