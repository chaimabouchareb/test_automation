public class Car {
    // Fields (attributes)
    private String model;
    private int year;
    private double mileage;
  
    // Constructor
    public Car(String model, int year, double mileage) {
      this.model = model;
      this.year = year;
      this.mileage = mileage;
    }
  
    // Methods (behaviors)
    public void drive() {
      System.out.println("The car is driving!");
    }
  
    public void getDetails() {
      System.out.println("Model: " + model + ", Year: " + year + ", Mileage: " + mileage);
    }
  }
  