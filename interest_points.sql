-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 16, 2023 at 09:35 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `interest_points`
--

-- --------------------------------------------------------

--
-- Table structure for table `interest_points_table`
--

CREATE TABLE `interest_points_table` (
  `id` int(11) NOT NULL,
  `subcat_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `interest_points` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `interest_points_table`
--

INSERT INTO `interest_points_table` (`id`, `subcat_id`, `date`, `interest_points`) VALUES
(1, 1, '2023-02-01', 30),
(2, 2, '2023-02-01', 100),
(3, 3, '2023-02-01', 40),
(4, 3, '2023-01-02', 50),
(5, 9, '2023-02-02', 60),
(6, 2, '2023-02-02', 10),
(7, 7, '2023-02-02', 40),
(8, 5, '2023-03-03', 40),
(9, 3, '2023-03-03', 30),
(10, 10, '2023-03-03', 10),
(11, 6, '2023-04-03', 60),
(12, 3, '2023-04-03', 70),
(13, 7, '2023-05-03', 20),
(14, 5, '2023-05-03', 40),
(15, 9, '2023-05-03', 60),
(16, 2, '2023-05-03', 100),
(17, 5, '2023-05-03', 30),
(18, 8, '2023-06-03', 70),
(19, 6, '2023-06-03', 80),
(20, 4, '2023-07-03', 20),
(21, 3, '2023-07-03', 40),
(22, 2, '2023-07-03', 50),
(23, 7, '2023-07-03', 50),
(24, 4, '2023-07-03', 100),
(25, 10, '2023-07-03', 10),
(26, 9, '2023-08-03', 40),
(27, 8, '2023-08-03', 50),
(28, 9, '2023-08-03', 60),
(29, 1, '2023-08-03', 70),
(30, 4, '2023-08-03', 80),
(31, 6, '2023-08-03', 10),
(32, 8, '2023-08-03', 90),
(33, 5, '2023-08-03', 80),
(34, 3, '2023-08-03', 70),
(35, 6, '2023-08-03', 60),
(36, 10, '2023-09-03', 50),
(37, 1, '2023-09-03', 10),
(38, 4, '2023-09-03', 70),
(39, 3, '2023-09-03', 40),
(40, 7, '2023-09-03', 30),
(41, 4, '2023-09-03', 20),
(42, 8, '2023-09-03', 60),
(43, 6, '2023-09-03', 70),
(44, 4, '2023-10-03', 90),
(45, 6, '2023-10-03', 100),
(46, 3, '2023-10-03', 10),
(47, 8, '2023-10-03', 40),
(48, 3, '2023-10-03', 20),
(49, 5, '2023-10-03', 30);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `interest_points_table`
--
ALTER TABLE `interest_points_table`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `interest_points_table`
--
ALTER TABLE `interest_points_table`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
