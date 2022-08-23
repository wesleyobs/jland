package {{full_package_name}};

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;

@SpringBootTest
public class ApplicationTest {
    @Autowired
    private Application application;


    @Test
    public void testApplicationSuccess() {
        assertTrue(this.application != null);
    }
}