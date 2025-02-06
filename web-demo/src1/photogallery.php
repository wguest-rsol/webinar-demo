<?php
$images = [
    'Flower' => 'http://127.0.0.1/images/flower.jpg',
    'Sandbox' => 'http://127.0.0.1/images/sandbox.jpg',
    'Dog' => 'http://127.0.0.1/images/dog.jpg'
];

if (isset($_GET['image'])) {
    $imageUrl = $_GET['image'];
    
    $ch = curl_init($imageUrl);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    $response = curl_exec($ch);
    $contentType = curl_getinfo($ch, CURLINFO_CONTENT_TYPE);
    curl_close($ch);
    
    if ($response) {
        header('Content-Type: ' . $contentType);
        echo $response;
        exit;
    } else {
        http_response_code(404);
        echo "Image not found.";
        exit;
    }
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image List</title>
    <script src="https://cdn.jsdelivr.net/npm/vue@3/dist/vue.global.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            height: 100vh;
            background-color: #f4f4f4;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background: white;
            padding: 10px;
            margin: 5px 0;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        a {
            text-decoration: none;
            color: #333;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div id="app">
        <h1>Available Images</h1>
        <ul>
            <li v-for="(file, name) in images" :key="name">
                <a :href="'?image=' + encodeURIComponent(file)" target="_blank">{{ name }}</a>
            </li>
        </ul>
    </div>
    <script>
        const { createApp } = Vue;
        createApp({
            data() {
                return {
                    images: {
                        'Flower': 'http://localhost/images/flower.jpg',
                        'Sandbox': 'http://localhost/images/sandbox.jpg',
                        'Dog': 'http://localhost/images/dog.jpg'
                    }
                };
            }
        }).mount('#app');
    </script>
</body>
</html>
