-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 12, 2018 at 09:41 AM
-- Server version: 5.7.22-0ubuntu0.16.04.1
-- PHP Version: 7.0.28-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `eleicao`
--

-- --------------------------------------------------------

--
-- Table structure for table `eleitores`
--

CREATE TABLE `eleitores` (
  `id_eleitor` int(11) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `nome` varchar(45) DEFAULT NULL,
  `sobrenome` varchar(255) NOT NULL,
  `data_nascimento` varchar(45) NOT NULL,
  `telefone_celular` varchar(45) DEFAULT NULL,
  `cep` varchar(45) NOT NULL,
  `zona` varchar(45) DEFAULT NULL,
  `votou` tinyint(4) DEFAULT '0',
  `digital` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `eleitores`
--

INSERT INTO `eleitores` (`id_eleitor`, `cpf`, `nome`, `sobrenome`, `data_nascimento`, `telefone_celular`, `cep`, `zona`, `votou`, `digital`) VALUES
(1, '10911109809', 'Joseph', 'Magno', '28/02/1993', '31983160034', '36309010', '78', 0, '139110'),
(2, '10911109817', 'Alexia', 'Barbosa', '28/02/1995', '31983160034', '36309016', '78', 0, '281562'),
(3, '18911109817', 'Lucas', 'Fernandes', '17/06/1994', '3183145260', '36309025', '78', 0, '114952');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `eleitores`
--
ALTER TABLE `eleitores`
  ADD PRIMARY KEY (`id_eleitor`,`cpf`,`cep`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `eleitores`
--
ALTER TABLE `eleitores`
  MODIFY `id_eleitor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
