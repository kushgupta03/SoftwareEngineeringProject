const express = require("express");
const app = express();
const mongoose = require("mongoose");
const cors = require("cors");

app.use(cors());
app.use(express.json());

mongoose
  .connect("mongodb://localhost:27017/tptptptp", { useNewUrlParser: true }) //mongodb://localhost:27017/yourDB
  .then(() => console.log("Connected to MongoDB..."))
  .catch((err) => console.error(err));

const UserScheme = new mongoose.Schema({
  username: { type: String, unique: true },
  password: { type: String },
});

const User = mongoose.model("User", UserScheme);

app.post("/register", async (req, res) => {
  const { username, password } = req.body;
  const user = new User({ username, password });
  const createdUser = await user.save();
  res.status(201).json(createdUser); // Sending the created user as the response
});

app.post("/login", async (req, res) => {
  const { username, password } = req.body;

  try {
    const user = await User.findOne({ username, password });

    if (!user) {
      return res.status(404).json({ error: "Invalid username or password" });
    }

    res.status(200).json({ message: "Login successful", user });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Server error" });
  }
});

const port = process.env.PORT || 8000;

app.listen(port, () => console.log(`Server running on port ${port} 🔥`));
