-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 14, 2019 at 02:26 AM
-- Server version: 10.1.25-MariaDB
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `showcase_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `humidity_log`
--

CREATE TABLE `humidity_log` (
  `id` int(11) NOT NULL,
  `time` datetime NOT NULL,
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `settings`
--

CREATE TABLE `settings` (
  `relay_id` int(11) NOT NULL,
  `enable` int(11) NOT NULL,
  `sensor_type` int(11) NOT NULL,
  `on_value` int(11) NOT NULL,
  `off_value` int(11) NOT NULL,
  `status` int(11) NOT NULL,
  `manual` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `settings`
--

INSERT INTO `settings` (`relay_id`, `enable`, `sensor_type`, `on_value`, `off_value`, `status`, `manual`) VALUES
(1, 0, 1, 35, 30, 0, 0),
(2, 0, 0, 20, 17, 0, 0),
(3, 0, 0, 0, 0, 0, 0),
(4, 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `temp_log`
--

CREATE TABLE `temp_log` (
  `id` int(11) NOT NULL,
  `time` datetime NOT NULL,
  `value` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `humidity_log`
--
ALTER TABLE `humidity_log`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `settings`
--
ALTER TABLE `settings`
  ADD PRIMARY KEY (`relay_id`);

--
-- Indexes for table `temp_log`
--
ALTER TABLE `temp_log`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `humidity_log`
--
ALTER TABLE `humidity_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `settings`
--
ALTER TABLE `settings`
  MODIFY `relay_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `temp_log`
--
ALTER TABLE `temp_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
