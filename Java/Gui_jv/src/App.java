import javax.swing.JOptionPane;
public class App {
    public static void main(String[] args) throws Exception {
        //System.out.println("Hello, World!");
        String name = JOptionPane.showInputDialog("Enter your name");
        JOptionPane.showMessageDialog(null,"hello "+name);
        int age = Integer.parseInt(JOptionPane.showInputDialog("enter your age"));
        JOptionPane.showMessageDialog(null, "you are "+age+" years old");
        double height = Double.parseDouble(JOptionPane.showInputDialog("what is your height"));
        JOptionPane.showMessageDialog(null,"your name is "+name+" your age is "+age+" your height is "+height);
    }
}
