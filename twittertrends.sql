-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 16, 2019 at 09:48 PM
-- Server version: 5.7.27-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `twittertrends`
--
CREATE DATABASE IF NOT EXISTS `twittertrends` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `twittertrends`;

-- --------------------------------------------------------

--
-- Table structure for table `capture`
--

CREATE TABLE `capture` (
  `idCapture` int(11) NOT NULL,
  `nickname` varchar(100) DEFAULT NULL,
  `user` varchar(100) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `dateString` varchar(255) DEFAULT NULL,
  `geoLocation` varchar(255) DEFAULT NULL,
  `geoGeo` varchar(255) DEFAULT NULL,
  `geoCoordinates` varchar(255) DEFAULT NULL,
  `geoPlace` varchar(255) DEFAULT NULL,
  `lang` varchar(20) DEFAULT NULL,
  `followers` int(11) DEFAULT NULL,
  `friends` int(11) DEFAULT NULL,
  `points` int(11) NOT NULL DEFAULT '1',
  `description` varchar(255) DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `capture`
--
ALTER TABLE `capture`
  ADD PRIMARY KEY (`idCapture`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `capture`
--
ALTER TABLE `capture`
  MODIFY `idCapture` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=476278;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
