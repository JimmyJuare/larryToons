import React from "react";
import "./LandingPage.css";
const LandingPage = () => {
  return (
    <div>
      <h1 className="header">LarryToons Home</h1>
      <p>Welcome to the landing page!</p>
        <div className="image-container">
          
          <img
            className="images"
            src="https://larrys-books.s3.amazonaws.com/books/Blue_Lightning_Issue_2.png"
            alt="wither"
          />
          <img
            className="images"
            src="https://larrys-books.s3.amazonaws.com/books/IMG_20240306_180117.jpg"
            alt="wither"
          />
          <img
            className="images"
            src="https://larrys-books.s3.amazonaws.com/books/Untitled249_20230902165507.png"
            alt="wither"
          />
          <img
            className="images"
            src="https://larrys-books.s3.amazonaws.com/books/Wither_Issue_1.png"
            alt="wither"
          />
        </div>
    </div>
  );
};

export default LandingPage;
