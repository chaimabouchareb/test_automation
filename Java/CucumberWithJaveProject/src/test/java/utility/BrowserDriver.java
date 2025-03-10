package utility;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class BrowserDriver {
    public static WebDriver;

    public BrowserDriver(){
        this.driver = driver;
        System.setProperties("webdriver.chrome.driver", System.getProperties("user.dir")+"src/test/resources/drivers/chromedriver.exe");
        this.driver = new ChromeDriver();
    }

    public void close(){
        this.driver.close();
    }
}
