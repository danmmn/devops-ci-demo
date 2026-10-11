FROM nginx:alpine
# 自定义首页
RUN echo "<h1>GitHub Actions + Kind CI Demo</h1>" > /usr/share/nginx/html/index.html
EXPOSE 80
