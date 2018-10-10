-- phpMyAdmin SQL Dump
-- version 4.0.10.19
-- https://www.phpmyadmin.net
--
-- Host: updb1.up.ist.psu.edu
-- Generation Time: Oct 10, 2018 at 07:12 PM
-- Server version: 5.1.49-community
-- PHP Version: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `rjh5740`
--

-- --------------------------------------------------------

--
-- Table structure for table `orderdetails`
--

CREATE TABLE IF NOT EXISTS `orderdetails` (
  `ORDERID` int(11) NOT NULL,
  `PRODUCTID` int(11) NOT NULL,
  PRIMARY KEY (`ORDERID`,`PRODUCTID`),
  KEY `PRODUCT_FK` (`PRODUCTID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orderdetails`
--

INSERT INTO `orderdetails` (`ORDERID`, `PRODUCTID`) VALUES
(1, 2),
(1, 3);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orderdetails`
--
ALTER TABLE `orderdetails`
  ADD CONSTRAINT `ORDID_FK` FOREIGN KEY (`ORDERID`) REFERENCES `products` (`ProductID`),
  ADD CONSTRAINT `PRODUCT_FK` FOREIGN KEY (`PRODUCTID`) REFERENCES `orders` (`ORDERID`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
