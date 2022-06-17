-- phpMyAdmin SQL Dump
-- version 5.0.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 03, 2020 at 01:41 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `online organic health food store`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_page`
--

CREATE TABLE `admin_page` (
  `A_Id` int(10) NOT NULL,
  `A_Email` varchar(20) NOT NULL,
  `A_Password` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_page`
--

INSERT INTO `admin_page` (`A_Id`, `A_Email`, `A_Password`) VALUES
(1, 'admin', 1234);

-- --------------------------------------------------------

--
-- Table structure for table `charges_table`
--

CREATE TABLE `charges_table` (
  `C_Id` int(10) NOT NULL,
  `C_Delivary` int(10) NOT NULL,
  `C_Packing` int(10) NOT NULL,
  `C_Gst` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `charges_table`
--

INSERT INTO `charges_table` (`C_Id`, `C_Delivary`, `C_Packing`, `C_Gst`) VALUES
(1, 40, 40, 10);

-- --------------------------------------------------------

--
-- Table structure for table `food_table`
--

CREATE TABLE `food_table` (
  `f_ID` int(10) NOT NULL,
  `f_NAME` varchar(100) NOT NULL,
  `f_PRICE` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `food_table`
--

INSERT INTO `food_table` (`f_ID`, `f_NAME`, `f_PRICE`) VALUES
(1, 'Pasta', 200),
(2, 'Veg biriyani', 400),
(3, 'French Fries', 100),
(5, 'Fried Rice', 200),
(6, 'Pizza', 300),
(7, 'Apple Pie', 300),
(8, 'Tacos', 500),
(9, 'salsa', 100),
(10, 'salad', 600),
(11, 'Donuts', 300),
(12, 'Mac and Cheese', 300);

-- --------------------------------------------------------

--
-- Table structure for table `order_table`
--

CREATE TABLE `order_table` (
  `O_Id` int(10) NOT NULL,
  `O_Name` varchar(50) NOT NULL,
  `O_Price` int(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `order_table`
--

INSERT INTO `order_table` (`O_Id`, `O_Name`, `O_Price`) VALUES
(101, 'Pasta', 200),
(102, 'Veg biriyani', 400);

-- --------------------------------------------------------

--
-- Table structure for table `register_table`
--

CREATE TABLE `register_table` (
  `id` int(10) NOT NULL,
  `F_name` varchar(50) NOT NULL,
  `L_name` varchar(50) NOT NULL,
  `Email_id` varchar(50) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `Number` int(10) NOT NULL,
  `Address1` varchar(100) NOT NULL,
  `Address2` varchar(100) NOT NULL,
  `Town` varchar(50) NOT NULL,
  `Region` varchar(50) NOT NULL,
  `Zipcode` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register_table`
--

INSERT INTO `register_table` (`id`, `F_name`, `L_name`, `Email_id`, `Password`, `Number`, `Address1`, `Address2`, `Town`, `Region`, `Zipcode`) VALUES
(1, 'user', 'user', 'user', '1234', 123456789, 'india', 'india', 'india', 'india', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_page`
--
ALTER TABLE `admin_page`
  ADD PRIMARY KEY (`A_Id`);

--
-- Indexes for table `charges_table`
--
ALTER TABLE `charges_table`
  ADD PRIMARY KEY (`C_Id`);

--
-- Indexes for table `food_table`
--
ALTER TABLE `food_table`
  ADD PRIMARY KEY (`f_ID`);

--
-- Indexes for table `order_table`
--
ALTER TABLE `order_table`
  ADD PRIMARY KEY (`O_Id`);

--
-- Indexes for table `register_table`
--
ALTER TABLE `register_table`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_page`
--
ALTER TABLE `admin_page`
  MODIFY `A_Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `charges_table`
--
ALTER TABLE `charges_table`
  MODIFY `C_Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `food_table`
--
ALTER TABLE `food_table`
  MODIFY `f_ID` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `order_table`
--
ALTER TABLE `order_table`
  MODIFY `O_Id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=103;

--
-- AUTO_INCREMENT for table `register_table`
--
ALTER TABLE `register_table`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
