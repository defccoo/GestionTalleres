-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 27-03-2018 a las 19:14:28
-- Versión del servidor: 10.1.31-MariaDB
-- Versión de PHP: 7.2.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `talleres`
--
CREATE DATABASE IF NOT EXISTS `talleres` DEFAULT CHARACTER SET utf16 COLLATE utf16_spanish2_ci;
USE `talleres`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos`
--

DROP TABLE IF EXISTS `alumnos`;
CREATE TABLE `alumnos` (
  `DNI` int(8) NOT NULL,
  `Exp` varchar(10) COLLATE utf16_spanish2_ci NOT NULL,
  `Nombre` varchar(50) COLLATE utf16_spanish2_ci NOT NULL,
  `Ape1` varchar(50) COLLATE utf16_spanish2_ci NOT NULL,
  `Ape2` varchar(50) COLLATE utf16_spanish2_ci DEFAULT NULL,
  `Passwd` varchar(10) COLLATE utf16_spanish2_ci NOT NULL,
  `curso` int(1) DEFAULT NULL,
  `nivel` varchar(10) COLLATE utf16_spanish2_ci DEFAULT NULL,
  `grupo` varchar(10) COLLATE utf16_spanish2_ci DEFAULT NULL,
  `activo` int(1) DEFAULT NULL,
  `idTaller` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish2_ci;

--
-- RELACIONES PARA LA TABLA `alumnos`:
--

--
-- Volcado de datos para la tabla `alumnos`
--

INSERT INTO `alumnos` (`DNI`, `Exp`, `Nombre`, `Ape1`, `Ape2`, `Passwd`, `curso`, `nivel`, `grupo`, `activo`, `idTaller`) VALUES
(14, '1', 'Francisco', 'Lopez', 'Sanchis', 'fran1', 1, 'B', 'A', 0, 1),
(15, '2', 'Pedro', 'Martinez', NULL, 'peter', 2, 'A', 'C', 0, 2),
(25, '3', 'Manolo', 'Perez', 'Aspar', 'manu', 2, 'C', 'B', 0, 2),
(31, '7', 'Ana', 'Bermejo', 'Beltan', 'anaber', 3, 'A', 'B', 0, 1),
(33, '4', 'Marcos', 'Heredia', 'Buendia', 'marcs', 1, 'C', 'A', 0, 1),
(36, '5', 'Guillermo', 'Toro', 'Fuentes', 'guille', 1, 'B', 'B', 1, 2),
(45, '6', 'Julia', 'Sanches', 'Guarner', 'juli', 2, 'B', 'A', 0, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos_taller`
--

DROP TABLE IF EXISTS `alumnos_taller`;
CREATE TABLE `alumnos_taller` (
  `dni_alum` int(8) NOT NULL,
  `idTaller` int(6) NOT NULL,
  `valorar` int(2) NOT NULL,
  `opinion` varchar(255) COLLATE utf16_spanish2_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish2_ci;

--
-- RELACIONES PARA LA TABLA `alumnos_taller`:
--   `dni_alum`
--       `alumnos` -> `DNI`
--   `idTaller`
--       `taller` -> `idTaller`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

DROP TABLE IF EXISTS `departamentos`;
CREATE TABLE `departamentos` (
  `idDepart` int(6) NOT NULL,
  `nombre` varchar(150) COLLATE utf16_spanish2_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish2_ci;

--
-- RELACIONES PARA LA TABLA `departamentos`:
--

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`idDepart`, `nombre`) VALUES
(1, 'Informatica'),
(2, 'Musica'),
(3, 'Historia');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesores`
--

DROP TABLE IF EXISTS `profesores`;
CREATE TABLE `profesores` (
  `dni` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf16_spanish2_ci DEFAULT NULL,
  `apellidos` varchar(150) COLLATE utf16_spanish2_ci NOT NULL,
  `idDepart` int(6) NOT NULL,
  `pass_prof` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish2_ci;

--
-- RELACIONES PARA LA TABLA `profesores`:
--   `idDepart`
--       `departamentos` -> `idDepart`
--

--
-- Volcado de datos para la tabla `profesores`
--

INSERT INTO `profesores` (`dni`, `nombre`, `apellidos`, `idDepart`, `pass_prof`) VALUES
(45, 'Julia', 'Sanches Guarner', 1, 0),
(50, 'Francisco', 'Lopez Sanchis', 1, 0),
(51, 'Pedro', 'Martinez peter', 1, 0),
(52, 'Manolo', 'Perez Aspar', 2, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prof_taller`
--

DROP TABLE IF EXISTS `prof_taller`;
CREATE TABLE `prof_taller` (
  `dni_prof` int(8) NOT NULL,
  `idTaller` int(6) NOT NULL,
  `fecha` date DEFAULT NULL,
  `horario_inicio` time DEFAULT NULL,
  `horario_fin` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish2_ci;

--
-- RELACIONES PARA LA TABLA `prof_taller`:
--   `dni_prof`
--       `profesores` -> `dni`
--   `idTaller`
--       `taller` -> `idTaller`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `taller`
--

DROP TABLE IF EXISTS `taller`;
CREATE TABLE `taller` (
  `idTaller` int(6) NOT NULL,
  `descrip` varchar(150) COLLATE utf16_spanish2_ci DEFAULT NULL,
  `idDepart` int(6) NOT NULL,
  `nivel` varchar(50) COLLATE utf16_spanish2_ci DEFAULT NULL,
  `curso` int(6) NOT NULL,
  `maxAlum` int(6) NOT NULL,
  `duracion` int(6) NOT NULL,
  `jornada` tinyint(1) DEFAULT NULL,
  `excede` tinyint(1) DEFAULT NULL,
  `foto_taller` varchar(255) COLLATE utf16_spanish2_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish2_ci;

--
-- RELACIONES PARA LA TABLA `taller`:
--

--
-- Volcado de datos para la tabla `taller`
--

INSERT INTO `taller` (`idTaller`, `descrip`, `idDepart`, `nivel`, `curso`, `maxAlum`, `duracion`, `jornada`, `excede`, `foto_taller`) VALUES
(1, 'TWIST & SHOUT', 1, 'ESO', 2, 25, 50, NULL, NULL, ''),
(2, 'COLLARES', 1, 'ESO', 1, 30, 60, NULL, NULL, '');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`DNI`),
  ADD KEY `IdTaller` (`idTaller`) USING BTREE;

--
-- Indices de la tabla `alumnos_taller`
--
ALTER TABLE `alumnos_taller`
  ADD PRIMARY KEY (`dni_alum`,`idTaller`),
  ADD KEY `idTaller` (`idTaller`);

--
-- Indices de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`idDepart`);

--
-- Indices de la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`dni`),
  ADD KEY `departamento` (`idDepart`);

--
-- Indices de la tabla `prof_taller`
--
ALTER TABLE `prof_taller`
  ADD PRIMARY KEY (`dni_prof`,`idTaller`),
  ADD KEY `idTaller` (`idTaller`);

--
-- Indices de la tabla `taller`
--
ALTER TABLE `taller`
  ADD PRIMARY KEY (`idTaller`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alumnos_taller`
--
ALTER TABLE `alumnos_taller`
  ADD CONSTRAINT `alumnos_taller_ibfk_1` FOREIGN KEY (`dni_alum`) REFERENCES `alumnos` (`DNI`),
  ADD CONSTRAINT `alumnos_taller_ibfk_2` FOREIGN KEY (`idTaller`) REFERENCES `taller` (`idTaller`);

--
-- Filtros para la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD CONSTRAINT `profesores_ibfk_1` FOREIGN KEY (`idDepart`) REFERENCES `departamentos` (`idDepart`);

--
-- Filtros para la tabla `prof_taller`
--
ALTER TABLE `prof_taller`
  ADD CONSTRAINT `prof_taller_ibfk_1` FOREIGN KEY (`dni_prof`) REFERENCES `profesores` (`dni`),
  ADD CONSTRAINT `prof_taller_ibfk_2` FOREIGN KEY (`idTaller`) REFERENCES `taller` (`idTaller`);


--
-- Metadatos
--
USE `phpmyadmin`;

--
-- Metadatos para la tabla alumnos
--

--
-- Metadatos para la tabla alumnos_taller
--

--
-- Metadatos para la tabla departamentos
--

--
-- Metadatos para la tabla profesores
--

--
-- Metadatos para la tabla prof_taller
--

--
-- Metadatos para la tabla taller
--

--
-- Metadatos para la base de datos talleres
--

--
-- Volcado de datos para la tabla `pma__pdf_pages`
--

INSERT INTO `pma__pdf_pages` (`db_name`, `page_descr`) VALUES
('talleres', 'Relaciones Talleres');

SET @LAST_PAGE = LAST_INSERT_ID();

--
-- Volcado de datos para la tabla `pma__table_coords`
--

INSERT INTO `pma__table_coords` (`db_name`, `table_name`, `pdf_page_number`, `x`, `y`) VALUES
('talleres', 'alumnos', @LAST_PAGE, 73, 233),
('talleres', 'alumnos_taller', @LAST_PAGE, 307, 182),
('talleres', 'departamentos', @LAST_PAGE, 333, 66),
('talleres', 'prof_taller', @LAST_PAGE, 303, 325),
('talleres', 'profesores', @LAST_PAGE, 62, 80),
('talleres', 'taller', @LAST_PAGE, 537, 228);

--
-- Volcado de datos para la tabla `pma__central_columns`
--

INSERT INTO `pma__central_columns` (`db_name`, `col_name`, `col_type`, `col_length`, `col_collation`, `col_isNull`, `col_extra`, `col_default`) VALUES
('talleres', 'pass_prof', 'int', '11', '', 0, ',', '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
