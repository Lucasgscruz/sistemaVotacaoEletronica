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
(3, '18911109817', 'Lucas', 'Fernandes', '17/06/1994', '3183145260', '36309025', '78', 0, '114952'),
(5, '1095135', 'Alexandre', 'Bittencourt', '28/02/1994', '31983160034', '78', 0, '114952'),
(6, '1095136', 'Carolina', 'Ribeiro', '28/02/1994', '31983160034', '78', 0, '114952'),
(7, '1095137', 'Charles', 'Figueredo', '28/02/1994', '31983160034', '78', 0, '114952'),
(8, '1095138', 'Daniel', 'Guidoni', '28/02/1994', '31983160034', '78', 0, '114952'),
(9, '1095139', 'Daniel', 'Madeira', '28/02/1994', '31983160034', '78', 0, '114952'),
(10, '10951310', 'Darlinton', 'Barbosa', '28/02/1994', '31983160034', '78', 0, '114952'),
(11, '10951311', 'Diego', 'Roberto', '28/02/1994', '31983160034', '78', 0, '114952'),
(12, '10951312', 'Edimilson', 'Batista', '28/02/1994', '31983160034', '78', 0, '114952'),
(13, '10951313', 'Elder', 'Cirilo', '28/02/1994', '31983160034', '78', 0, '114952'),
(14, '10951314', 'Elisa', 'Albergaria', '28/02/1994', '31983160034', '78', 0, '114952'),
(15, '10951315', 'Elverton', 'Carvalho', '28/02/1994', '31983160034', '78', 0, '114952'),
(16, '10951316', 'Fernanda', 'Sumika', '28/02/1994', '31983160034', '78', 0, '114952'),
(17, '10951317', 'Flavio', 'Luiz', '28/02/1994', '31983160034', '78', 0, '114952'),
(18, '10951318', 'Leonardo', 'Rocha', '28/02/1994', '31983160034', '78', 0, '114952'),
(19, '10951319', 'Marcos', 'Laia', '28/02/1994', '31983160034', '78', 0, '114952'),
(20, '10951320', 'Matheus', 'Carvalho', '28/02/1994', '31983160034', '78', 0, '114952'),
(21, '10951321', 'Michelli', 'Marlane', '28/02/1994', '31983160034', '78', 0, '114952'),
(22, '10951322', 'Milene', 'Barbosa', '28/02/1994', '31983160034', '78', 0, '114952'),
(23, '10951323', 'Rafael', 'Sachetto', '28/02/1994', '31983160034', '78', 0, '114952'),
(24, '10951324', 'Sofia', 'Larissa', '28/02/1994', '31983160034', '78', 0, '114952'),
(25, '10951325', 'Vinicius', 'Vieira', '28/02/1994', '31983160034', '78', 0, '114952'),
(26, '10951326', 'Vinicius', 'Durelli', '28/02/1994', '31983160034', '78', 0, '114952'),
(27, '10951327', 'Arthur', 'Rodrigues', '28/02/1994', '31983160034', '78', 0, '114952'),
(28, '10951328', 'Carlos', 'Magno', '28/02/1994', '31983160034', '78', 0, '114952'),
(29, '10951329', 'Diego', 'Freire', '28/02/1994', '31983160034', '78', 0, '114952'),
(30, '10951330', 'Diego', 'Lucio', '28/02/1994', '31983160034', '78', 0, '114952'),
(31, '10951331', 'Gustavo', 'Detomi', '28/02/1994', '31983160034', '78', 0, '114952'),
(32, '10951332', 'Iago', 'Alvarenga', '28/02/1994', '31983160034', '78', 0, '114952'),
(33, '10951333', 'Igor', 'Santana', '28/02/1994', '31983160034', '78', 0, '114952'),
(34, '10951334', 'Joao', 'Pedro', '28/02/1994', '31983160034', '78', 0, '114952'),
(35, '10951335', 'Leandro', 'Campos', '28/02/1994', '31983160034', '78', 0, '114952'),
(36, '10951336', 'Lucas', 'Geraldo', '28/02/1994', '31983160034', '78', 0, '114952'),
(37, '10951337', 'Luiz', 'Felipe', '28/02/1994', '31983160034', '78', 0, '114952'),
(38, '10951338', 'Maria', 'Emilia', '28/02/1994', '31983160034', '78', 0, '114952'),
(39, '10951339', 'Matheus', 'Reis', '28/02/1994', '31983160034', '78', 0, '114952'),
(40, '10951340', 'Maycon', 'Ferreira', '28/02/1994', '31983160034', '78', 0, '114952'),
(41, '10951341', 'Millas', 'Nasser', '28/02/1994', '31983160034', '78', 0, '114952'),
(42, '10951342', 'Rafael', 'Henrique', '28/02/1994', '31983160034', '78', 0, '114952'),
(43, '10951343', 'Remo', 'Gresta', '28/02/1994', '31983160034', '78', 0, '114952'),
(44, '10951344', 'Rodrigo', 'Ferreira', '28/02/1994', '31983160034', '78', 0, '114952'),
(45, '10951345', 'Samuel', 'Ribeiro', '28/02/1994', '31983160034', '78', 0, '114952'),
(46, '10951346', 'Savyo', 'Toledo', '28/02/1994', '31983160034', '78', 0, '114952'),
(47, '10951347', 'Thiago', 'Escarassati', '28/02/1994', '31983160034', '78', 0, '114952'),
(48, '10951348', 'Tulio', 'Ribeiro', '28/02/1994', '31983160034', '78', 0, '114952'),
(49, '10951349', 'Vinicius', 'Marques', '28/02/1994', '31983160034', '78', 0, '114952'),
(50, '10951350', 'Ygor', 'Henrique', '28/02/1994', '31983160034', '78', 0, '114952');


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
