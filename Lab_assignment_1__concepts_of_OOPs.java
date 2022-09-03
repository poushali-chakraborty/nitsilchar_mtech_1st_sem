/* 
Lab assignment 1: Concepts of Object Oriented Programming implemented in a single program.
 * Encapsulation is one of the key features of object-oriented programming. Encapsulation refers to the bundling of fields and methods inside a single class.

It prevents outer classes from accessing and changing fields and methods of a class. This also helps to achieve data hiding.
 */
class Color{
    private int r,g,b;

    public int getR() {
        return r;
    }

    public void setR(int r) {
        this.r = r;
    }

    public int getG() {
        return g;
    }

    public void setG(int g) {
        this.g = g;
    }

    public int getB() {
        return b;
    }

    public void setB(int b) {
        this.b = b;
    }
 /**    A constructor in Java is similar to a method that is invoked when an object of the class is created.

    Unlike Java methods, a constructor has the same name as that of the class and does not have any return type.
 
 */
   public Color() { //default constructor
        this.r = 255;
        this.g = 255;
        this.b = 255;
    }

    public Color(int r, int g, int b) { //parameterized constructor
        this.r = r;
        this.g = g;
        this.b = b;
    }
    /**
     * A destructor is a special method that gets called automatically as soon as the life-cycle of an object is finished.
     *  A destructor is called to de-allocate and free memory.
     */
    public void finalize() throws Throwable  
    {  
    System.out.println("Object color is destroyed by the Garbage Collector");  
    } 
    
    /**
     * In Java, two or more methods may have the same name if they differ in parameters (different number of parameters, different types of parameters, or both). 
     * These methods are called overloaded methods and this feature is called method overloading.
     */
    void showColor(int i){
        System.out.println("color: ("+r+","+g+","+b+")");
    }
    void showColor(String a){
        System.out.println("color:"+Integer.toHexString(r)+Integer.toHexString(g)+Integer.toHexString(b));
    }

}
/**
 * Inheritance is one of the key features of OOP that allows us to create a new class from an existing class.

The new class that is created is known as subclass (child or derived class) and the existing class from where the child class is derived is known as superclass (parent or base class).

The extends keyword is used to perform inheritance in Java. 
 */
class ColorwithAlpha extends Color{
    double a;

    public double getA() {
        return a;
    }

    public void setA(double a) {
        this.a = a;
    }
    ColorwithAlpha(int r, int g, int b,double d){
        super(r,g,b); //the super keyword is used to call the method of the parent class from the method of the child class
        this.a=d;
    }
}

/*
 * Data abstraction is the process of hiding certain details and showing only essential information to the user.
Abstraction can be achieved with either abstract classes or interfaces .
 
An interface is a fully abstract class. It includes a group of abstract methods (methods without a body).
We use the interface keyword to create an interface in Java.
We cannot create objects of interfaces.

To use an interface, other classes must implement it. We use the implements keyword to implement an interface.
*/
interface Shape{
    int getDimension();
    
    void displayAllProperties();

}
//Abstract class: is a restricted class that cannot be used to create objects (to access it, it must be inherited from another class).
abstract class Shape2d implements Shape{
    int no_of_sides;
    abstract double getArea();
    abstract double getPerimeter();
    public int getDimension(){
        return 2;
    }
    @Override
    public void displayAllProperties() {
        System.out.println(getDimension()+"d Shape, sides:"+no_of_sides+", area:"+getArea()+", perimeter:"+getPerimeter());
        
    }

}
class Rectangle extends Shape2d{
    private int height, width;

    Rectangle(int h,int w){
        this.height=h;
        this.width=w;
        this.no_of_sides=4;
    }

    @Override
    double getArea() {

        return height*width;
    }

    @Override
    double getPerimeter() {
        
        return 2*(height+width);
    }
    /**
     * If the same method is defined in both the superclass and the subclass, then the method of the subclass class overrides the method of the superclass.
     *  This is known as method overriding.
     */
    @Override
    public void displayAllProperties() {
        System.out.println("its a Rectangle");
        super.displayAllProperties();
       
    }
    
}
class Circle extends Shape2d{
    private int radius;

    Circle(int r){
        this.radius=r;
        this.no_of_sides=1;
    }


    @Override
    double getArea() {
        
        return (22/7)*radius*radius;
    }

    @Override
    double getPerimeter() {
        
        return 2*(22/7)*radius;
    }
    @Override
    public void displayAllProperties() {
        
        super.displayAllProperties();
        System.out.println("its a Circle");
    }

}

public class Oops {
    public static void main(String args[]){
        Color c1= new Color();
        Color c2= new Color(100,100,100);
        System.out.println(c1.getR()+","+c1.getG()+","+c1.getB());
        c1.showColor(0);
        System.out.println(c2.getR()+","+c2.getG()+","+c2.getB());
        c2.showColor("");

        c1=null;
        System.gc();
        //System.out.println(c1.getR()+","+c1.getG()+","+c1.getB());
        ColorwithAlpha c3= new ColorwithAlpha(200, 100, 20, 0.8);
        System.out.println(c3.getR()+","+c3.getG()+","+c3.getB()+","+ c3.getA());

        Rectangle rect= new Rectangle(5, 10);
        rect.displayAllProperties();

        Circle cir= new Circle(4);
        cir.displayAllProperties();
        

    }
}
