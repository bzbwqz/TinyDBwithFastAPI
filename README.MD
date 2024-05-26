# FastAPI with TinyDB CRUD Application

This project is a simple CRUD (Create, Read, Update, Delete) API built with FastAPI and TinyDB. It demonstrates how to integrate a TinyDB database with a FastAPI application to perform basic operations on a `Student` database table.

## Features

- **Create Student**: Add a new student record to the database.
- **Read Student**: Retrieve details of a specific student by their ID.
- **Update Student**: Modify an existing student's details.
- **Delete Student**: Remove a student record from the database.
- **List Students**: Get a list of all students in the database.

## Data Model

The `Student` data model includes the following fields:
- `id`: An auto-generated unique identifier for each student.
- `name`: The name of the student (string type).
- `age`: The age of the student (integer type).
- `grade`: The grade level of the student (enum type with options: Grade One, Grade Two, Grade Three).

## Endpoints

The API provides the following endpoints:
- `POST /students/`: Create a new student record.
- `GET /students/{student_id}`: Retrieve a specific student's details.
- `GET /students/`: Retrieve a list of all students.
- `PUT /students/{student_id}`: Update a specific student's details.
- `DELETE /students/{student_id}`: Delete a specific student record.

## Setup and Installation

To run this project, you will need to install the required dependencies listed in `requirements.txt`.

```shell
pip install -r requirements.txt
After installing the dependencies, you can start the FastAPI server with the following command:

uvicorn app:app --reload
The --reload flag enables auto-reloading of the server when code changes are detected.

## Usage
Once the server is running, you can access the API documentation and test the endpoints using the auto-generated Swagger UI at http://127.0.0.1:8000/docs.

## Deployment
This application can be deployed to cloud platforms like Azure Web App. Ensure that the platform supports Python and provides sufficient storage for the db.json file.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License
This project is open-sourced under the MIT License.


This `README.md` file provides an overview of the application, its features, the data model, available API endpoints, setup instructions, usage details, deployment notes, contribution guidelines, and licensing information. It's designed to give users and developers all the necessary information to understand and use the application effectively.

# FastAPI与TinyDB学生管理系统

本项目是一个基于FastAPI和TinyDB的学生管理系统，实现了学生信息的增删改查（CRUD）功能。

## 功能

- **创建学生**：添加新的学生记录。
- **读取学生**：通过ID获取特定学生的详细信息。
- **更新学生**：修改已有学生的信息。
- **删除学生**：移除学生记录。
- **列出所有学生**：获取所有学生的信息列表。

## 数据模型

学生信息包含以下字段：
- `id`：学生的唯一标识符。
- `name`：学生的姓名。
- `age`：学生的年龄。
- `grade`：学生的年级，可选值为`Grade One`、`Grade Two`、`Grade Three`。

## API端点

- `POST /students/`：创建学生记录。
- `GET /students/{student_id}`：获取特定学生信息。
- `GET /students/`：获取所有学生信息。
- `PUT /students/{student_id}`：更新特定学生信息。
- `DELETE /students/{student_id}`：删除特定学生记录。

## 安装

克隆仓库到本地后，安装依赖项：

```shell
pip install -r requirements.txt

## 运行
使用以下命令启动FastAPI服务器：

uvicorn app:app --reload

--reload 参数允许在检测到代码更改时自动重新加载服务器。

## 使用说明
服务器运行后，可以通过访问 http://127.0.0.1:8000/docs 使用Swagger UI测试API端点。

## 部署
本应用可以部署在支持Python的云平台上，如Azure Web App。确保云平台为 db.json 文件提供足够的存储空间。

## 贡献指南
欢迎对本项目做出贡献。请fork本仓库并提交您的更改。

## 许可证
本项目在MIT许可证下开源。


这个 `README.md` 文件提供了项目的详细介绍，包括其功能、数据模型、API端点、安装运行方法、使用说明、部署建议、贡献指南和许可信息。这样的文档能帮助用户和开发者更好地理解和使用这个学生管理系统。如果您有任何疑问或需要进一步的帮助，请随时告诉我。