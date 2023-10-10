-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2023-10-10 06:07:05
-- 伺服器版本： 10.4.24-MariaDB
-- PHP 版本： 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫: `jnc`
--

-- --------------------------------------------------------

--
-- 資料表結構 `alert_log`
--

CREATE TABLE `alert_log` (
  `id` varchar(50) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `event_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add 監測設備列表', 7, 'add_jncdevicemodel'),
(26, 'Can change 監測設備列表', 7, 'change_jncdevicemodel'),
(27, 'Can delete 監測設備列表', 7, 'delete_jncdevicemodel'),
(28, 'Can view 監測設備列表', 7, 'view_jncdevicemodel'),
(29, 'Can add 監測場域列表', 8, 'add_jncpositionmodel'),
(30, 'Can change 監測場域列表', 8, 'change_jncpositionmodel'),
(31, 'Can delete 監測場域列表', 8, 'delete_jncpositionmodel'),
(32, 'Can view 監測場域列表', 8, 'view_jncpositionmodel'),
(33, 'Can add 檢測數據列表', 9, 'add_jncinspectmodel'),
(34, 'Can change 檢測數據列表', 9, 'change_jncinspectmodel'),
(35, 'Can delete 檢測數據列表', 9, 'delete_jncinspectmodel'),
(36, 'Can view 檢測數據列表', 9, 'view_jncinspectmodel'),
(37, 'Can add 歷史檢測數據列表', 10, 'add_jncinspecthistorymodel'),
(38, 'Can change 歷史檢測數據列表', 10, 'change_jncinspecthistorymodel'),
(39, 'Can delete 歷史檢測數據列表', 10, 'delete_jncinspecthistorymodel'),
(40, 'Can view 歷史檢測數據列表', 10, 'view_jncinspecthistorymodel'),
(41, 'Can add 推播設備群組', 11, 'add_notifydevicemodel'),
(42, 'Can change 推播設備群組', 11, 'change_notifydevicemodel'),
(43, 'Can delete 推播設備群組', 11, 'delete_notifydevicemodel'),
(44, 'Can view 推播設備群組', 11, 'view_notifydevicemodel'),
(45, 'Can add 推播事件', 12, 'add_notifyeventmodel'),
(46, 'Can change 推播事件', 12, 'change_notifyeventmodel'),
(47, 'Can delete 推播事件', 12, 'delete_notifyeventmodel'),
(48, 'Can view 推播事件', 12, 'view_notifyeventmodel'),
(49, 'Can add 推播權杖儲存', 13, 'add_notifytokenmodel'),
(50, 'Can change 推播權杖儲存', 13, 'change_notifytokenmodel'),
(51, 'Can delete 推播權杖儲存', 13, 'delete_notifytokenmodel'),
(52, 'Can view 推播權杖儲存', 13, 'view_notifytokenmodel'),
(53, 'Can add 條件列表', 14, 'add_statement'),
(54, 'Can change 條件列表', 14, 'change_statement'),
(55, 'Can delete 條件列表', 14, 'delete_statement'),
(56, 'Can view 條件列表', 14, 'view_statement'),
(57, 'Can add 推播事件條件', 15, 'add_notifystatementmodel'),
(58, 'Can change 推播事件條件', 15, 'change_notifystatementmodel'),
(59, 'Can delete 推播事件條件', 15, 'delete_notifystatementmodel'),
(60, 'Can view 推播事件條件', 15, 'view_notifystatementmodel'),
(61, 'Can add 推播警告紀錄', 16, 'add_alertlogmodel'),
(62, 'Can change 推播警告紀錄', 16, 'change_alertlogmodel'),
(63, 'Can delete 推播警告紀錄', 16, 'delete_alertlogmodel'),
(64, 'Can view 推播警告紀錄', 16, 'view_alertlogmodel');

-- --------------------------------------------------------

--
-- 資料表結構 `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'devices_inspect', 'jncdevicemodel'),
(10, 'devices_inspect', 'jncinspecthistorymodel'),
(9, 'devices_inspect', 'jncinspectmodel'),
(8, 'devices_inspect', 'jncpositionmodel'),
(16, 'notify', 'alertlogmodel'),
(11, 'notify', 'notifydevicemodel'),
(12, 'notify', 'notifyeventmodel'),
(15, 'notify', 'notifystatementmodel'),
(13, 'notify', 'notifytokenmodel'),
(14, 'notify', 'statement'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- 資料表結構 `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-10-10 04:04:27.280420'),
(2, 'auth', '0001_initial', '2023-10-10 04:04:28.090773'),
(3, 'admin', '0001_initial', '2023-10-10 04:04:28.280401'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-10-10 04:04:28.288934'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-10-10 04:04:28.297251'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-10-10 04:04:28.369350'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-10-10 04:04:28.442866'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-10-10 04:04:28.464802'),
(9, 'auth', '0004_alter_user_username_opts', '2023-10-10 04:04:28.472506'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-10-10 04:04:28.533261'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-10-10 04:04:28.537020'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-10-10 04:04:28.545132'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-10-10 04:04:28.565420'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-10-10 04:04:28.586322'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-10-10 04:04:28.604616'),
(16, 'auth', '0011_update_proxy_permissions', '2023-10-10 04:04:28.612259'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-10-10 04:04:28.635259'),
(18, 'devices_inspect', '0001_initial', '2023-10-10 04:04:29.006453'),
(19, 'notify', '0001_initial', '2023-10-10 04:04:29.718163'),
(20, 'sessions', '0001_initial', '2023-10-10 04:04:29.778836');

-- --------------------------------------------------------

--
-- 資料表結構 `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `jnc_device`
--

CREATE TABLE `jnc_device` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `jnc_inspect`
--

CREATE TABLE `jnc_inspect` (
  `id` int(11) NOT NULL,
  `ChType` varchar(50) NOT NULL,
  `TagName` varchar(255) NOT NULL,
  `Unit` varchar(50) NOT NULL,
  `IsEnable` tinyint(1) NOT NULL,
  `Value` double NOT NULL,
  `AlarmState` varchar(50) NOT NULL,
  `IsRead` tinyint(1) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `device_id` int(11) DEFAULT NULL,
  `position_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `jnc_inspect_history`
--

CREATE TABLE `jnc_inspect_history` (
  `id` int(11) NOT NULL,
  `Unit` varchar(50) NOT NULL,
  `IsEnable` tinyint(1) NOT NULL,
  `Value` double NOT NULL,
  `AlarmState` varchar(50) NOT NULL,
  `IsRead` tinyint(1) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `inspect_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `jnc_position`
--

CREATE TABLE `jnc_position` (
  `id` int(11) NOT NULL,
  `DeviceName` varchar(255) NOT NULL,
  `JNCDevice` varchar(255) NOT NULL,
  `GPSx` decimal(9,6) NOT NULL,
  `GPSy` decimal(8,6) NOT NULL,
  `Connect` tinyint(1) NOT NULL,
  `USB` int(11) NOT NULL,
  `SIM` int(11) NOT NULL,
  `device_url` longtext NOT NULL,
  `inspect_url` longtext NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `notify_device`
--

CREATE TABLE `notify_device` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `ClientID` varchar(255) NOT NULL,
  `CallBackURL` longtext NOT NULL,
  `ClientSecret` longtext NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `token_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `notify_event`
--

CREATE TABLE `notify_event` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `message` longtext NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `device_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `notify_statement`
--

CREATE TABLE `notify_statement` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `statement` longtext NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `event_id` int(11) DEFAULT NULL,
  `jnc_inspect_id` int(11) DEFAULT NULL,
  `statement_id` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- 資料表結構 `notify_token`
--

CREATE TABLE `notify_token` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `token` longtext NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 傾印資料表的資料 `notify_token`
--

INSERT INTO `notify_token` (`id`, `name`, `token`, `created_at`, `updated_at`) VALUES
(1, '屏南', '123', '2023-10-10 12:06:52', '2023-10-10 12:06:57');

-- --------------------------------------------------------

--
-- 資料表結構 `statement`
--

CREATE TABLE `statement` (
  `id` varchar(50) NOT NULL,
  `name` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `updated_at` datetime NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `alert_log`
--
ALTER TABLE `alert_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `alert_log_event_id_5d70fae7_fk_notify_event_id` (`event_id`);

--
-- 資料表索引 `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- 資料表索引 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- 資料表索引 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- 資料表索引 `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- 資料表索引 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- 資料表索引 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- 資料表索引 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- 資料表索引 `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- 資料表索引 `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- 資料表索引 `jnc_device`
--
ALTER TABLE `jnc_device`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- 資料表索引 `jnc_inspect`
--
ALTER TABLE `jnc_inspect`
  ADD PRIMARY KEY (`id`),
  ADD KEY `jnc_inspect_device_id_031e2857_fk_jnc_device_id` (`device_id`),
  ADD KEY `jnc_inspect_position_id_5caed055_fk_jnc_position_id` (`position_id`);

--
-- 資料表索引 `jnc_inspect_history`
--
ALTER TABLE `jnc_inspect_history`
  ADD PRIMARY KEY (`id`),
  ADD KEY `jnc_inspect_history_inspect_id_812e5cc0_fk_jnc_inspect_id` (`inspect_id`);

--
-- 資料表索引 `jnc_position`
--
ALTER TABLE `jnc_position`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `notify_device`
--
ALTER TABLE `notify_device`
  ADD PRIMARY KEY (`id`),
  ADD KEY `notify_device_token_id_5cce5dd1_fk_notify_token_id` (`token_id`);

--
-- 資料表索引 `notify_event`
--
ALTER TABLE `notify_event`
  ADD PRIMARY KEY (`id`),
  ADD KEY `notify_event_device_id_412eb43c_fk_notify_device_id` (`device_id`);

--
-- 資料表索引 `notify_statement`
--
ALTER TABLE `notify_statement`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `jnc_inspect_id` (`jnc_inspect_id`),
  ADD KEY `notify_statement_event_id_d57b024b_fk_notify_event_id` (`event_id`),
  ADD KEY `notify_statement_statement_id_46941455_fk_statement_id` (`statement_id`);

--
-- 資料表索引 `notify_token`
--
ALTER TABLE `notify_token`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `statement`
--
ALTER TABLE `statement`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `jnc_device`
--
ALTER TABLE `jnc_device`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `jnc_inspect`
--
ALTER TABLE `jnc_inspect`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `jnc_inspect_history`
--
ALTER TABLE `jnc_inspect_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `jnc_position`
--
ALTER TABLE `jnc_position`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `notify_device`
--
ALTER TABLE `notify_device`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `notify_event`
--
ALTER TABLE `notify_event`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `notify_statement`
--
ALTER TABLE `notify_statement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `notify_token`
--
ALTER TABLE `notify_token`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `alert_log`
--
ALTER TABLE `alert_log`
  ADD CONSTRAINT `alert_log_event_id_5d70fae7_fk_notify_event_id` FOREIGN KEY (`event_id`) REFERENCES `notify_event` (`id`);

--
-- 資料表的限制式 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- 資料表的限制式 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- 資料表的限制式 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 資料表的限制式 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 資料表的限制式 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 資料表的限制式 `jnc_inspect`
--
ALTER TABLE `jnc_inspect`
  ADD CONSTRAINT `jnc_inspect_device_id_031e2857_fk_jnc_device_id` FOREIGN KEY (`device_id`) REFERENCES `jnc_device` (`id`),
  ADD CONSTRAINT `jnc_inspect_position_id_5caed055_fk_jnc_position_id` FOREIGN KEY (`position_id`) REFERENCES `jnc_position` (`id`);

--
-- 資料表的限制式 `jnc_inspect_history`
--
ALTER TABLE `jnc_inspect_history`
  ADD CONSTRAINT `jnc_inspect_history_inspect_id_812e5cc0_fk_jnc_inspect_id` FOREIGN KEY (`inspect_id`) REFERENCES `jnc_inspect` (`id`);

--
-- 資料表的限制式 `notify_device`
--
ALTER TABLE `notify_device`
  ADD CONSTRAINT `notify_device_token_id_5cce5dd1_fk_notify_token_id` FOREIGN KEY (`token_id`) REFERENCES `notify_token` (`id`);

--
-- 資料表的限制式 `notify_event`
--
ALTER TABLE `notify_event`
  ADD CONSTRAINT `notify_event_device_id_412eb43c_fk_notify_device_id` FOREIGN KEY (`device_id`) REFERENCES `notify_device` (`id`);

--
-- 資料表的限制式 `notify_statement`
--
ALTER TABLE `notify_statement`
  ADD CONSTRAINT `notify_statement_event_id_d57b024b_fk_notify_event_id` FOREIGN KEY (`event_id`) REFERENCES `notify_event` (`id`),
  ADD CONSTRAINT `notify_statement_jnc_inspect_id_971a7274_fk_jnc_inspect_id` FOREIGN KEY (`jnc_inspect_id`) REFERENCES `jnc_inspect` (`id`),
  ADD CONSTRAINT `notify_statement_statement_id_46941455_fk_statement_id` FOREIGN KEY (`statement_id`) REFERENCES `statement` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
