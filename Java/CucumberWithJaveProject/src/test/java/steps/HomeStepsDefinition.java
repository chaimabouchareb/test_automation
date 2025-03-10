package steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.junit.Assert;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class HomeStepsDefinition {
    public static WebDriver driver;

    @Given("I navigate to the home page")
    public void i_navigate_to_the_home_page() {
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-allow-origins=*");
        System.setProperties("webdriver.chrome.driver","C:\\webdrivers");
        driver = new ChromeDriver(options);
        driver.get("https://mail.rediff.com/cgi-bin/login.cgi");
        throw new io.cucumber.java.PendingException();
    }
    @When("Navigate Forgot password link")
    public void navigate_forgot_password_link() {
        driver.findElement(By.xpath("//u[text()='Forgot Password?']")).click();
        throw new io.cucumber.java.PendingException();

    }
    @Then("I should see forgot password page")
    public void i_should_see_forgot_password_page() {
        Thread.sleep(5000);
        Assert.assertEquals(driver.getTitle(), "Password help assistance");
        throw new io.cucumber.java.PendingException();

    }

}
