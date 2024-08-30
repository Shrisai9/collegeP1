<?php
    $firstName = $_POST['firstName'];
    $lastName = $_POST['lastName'];
    $gender = $_POST['gender'];
    $age = (int) $_POST['age']; // Ensure age is an integer
    $date = $_POST['date'];

    // Validate and sanitize user input
    $firstName = filter_var($firstName, FILTER_SANITIZE_STRING);
    $lastName = filter_var($lastName, FILTER_SANITIZE_STRING);
    $gender = filter_var($gender, FILTER_SANITIZE_STRING);
    $date = filter_var($date, FILTER_SANITIZE_STRING);

    // Database connection
    $conn = new mysqli('localhost', 'root', '', 'registraion form revsol');
    if ($conn->connect_error) {
        die('Connection failed : '. $conn->connect_error);
    } else {
        $stmt = $conn->prepare("insert into registration(firstName, lastName, gender, age, date) values(?,?,?,?,?)");
        $stmt->bind_param("sssis", $firstName, $lastName, $gender, $age, $date);
        try {
            $stmt->execute();
            echo "Registration successfully...";
        } catch (Exception $e) {
            echo "Error: ". $e->getMessage();
        }
        $stmt->close();
        $conn->close();
    }
?>