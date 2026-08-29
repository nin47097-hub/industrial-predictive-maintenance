const express = require("express");
const cors = require("cors");

const predictionsRoutes = require("./Routes/predictionsroutes");

const app = express();

const PORT = process.env.PORT || 3000;

app.use(cors());

app.use(express.json());

app.use("/api", predictionsRoutes);

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
