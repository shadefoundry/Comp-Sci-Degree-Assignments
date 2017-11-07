-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Mar 21, 2016 at 04:44 PM
-- Server version: 5.7.9
-- PHP Version: 5.6.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Assignment_7`
--

-- --------------------------------------------------------

--
-- Table structure for table `assignment_7`
--

DROP TABLE IF EXISTS `assignment_7`;
CREATE TABLE IF NOT EXISTS `assignment_7` (
  `IDNumber` int(11) NOT NULL AUTO_INCREMENT,
  `FirstName` text NOT NULL,
  `LastName` text NOT NULL,
  `BirthDate` text NOT NULL,
  PRIMARY KEY (`IDNumber`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `assignment_7`
--

INSERT INTO `assignment_7` (`IDNumber`, `FirstName`, `LastName`, `BirthDate`) VALUES
(1, 'Kevin', 'Lopez', '1/1/1997'),
(2, 'Kevin', 'Lopez', '1/1/1997'),
(3, 'Oleg', 'Lukyanenko', '11/22/1997'),
(4, 'Erik', 'Lopez', '1/24/2004'),
(5, 'Andrew', 'Jiang', '9/17/1997');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
