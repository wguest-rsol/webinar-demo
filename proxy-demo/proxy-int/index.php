<?php
header("Content-Type: text/html; charset=UTF-8");
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fake Secret Portal</title>
    <script src="https://cdn.jsdelivr.net/npm/vue@3/dist/vue.global.prod.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .header, .footer {
            background: #333;
            color: white;
            text-align: center;
            padding: 15px 0;
            font-size: 1.2em;
        }
        .container {
            max-width: 600px;
            margin: 50px auto;
            text-align: center;
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .secret {
            margin-top: 20px;
            font-weight: bold;
            color: red;
        }
        button {
            padding: 10px 15px;
            font-size: 1em;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 10px;
        }
        button:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <div class="header">Fake Secret Portal</div>
    <div id="app" class="container">
        <h1>Welcome to the Portal</h1>
        <p>Your gateway to exclusive information.</p>
        <button @click="showSecret = !showSecret">Toggle Secret</button>
        <p v-if="showSecret" class="secret">🚀 Top Secret Content: 42-Alpha-X</p>
    </div>
    <div class="footer">&copy; 2025 Fake Corp. All rights reserved.</div>
    <script>
        const { createApp, ref } = Vue;
        createApp({
            setup() {
                const showSecret = ref(false);
                return { showSecret };
            }
        }).mount("#app");
    </script>
</body>
</html>
