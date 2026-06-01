#include <opencv2/opencv.hpp>
#include <iostream>

int main(int argc, char** argv) {
    // 读取图片（请在 test_images 里放一张图片，或指定绝对路径）
    std::string imgPath = "test_images/sample.jpg";
    cv::Mat image = cv::imread(imgPath);
    if (image.empty()) {
        std::cerr << "Could not read image: " << imgPath << std::endl;
        return -1;
    }

    // 显示图片
    cv::imshow("Display Image", image);
    cv::waitKey(0);  // 等待按键

    return 0;
}
