from applications import create_app

app = create_app()


if __name__ == '__main__':
    print(app.url_map)  # 输出所有接口
    app.run(debug=True)
