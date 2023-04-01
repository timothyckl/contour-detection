#include <opencv2/opencv.hpp>
#include <iostream>

using namespace std;
// not using cv namespace to get familiar with library functions/features

int main() {
  // 1) read image and convert to grayscale 
  cv::Mat image = cv::imread("./assets/image_with_objects.jpg");
  
  cv::Mat grayscaled_image;
  cv::cvtColor(image, grayscaled_image, cv::COLOR_BGR2GRAY);

  // 2) apply binary thresholding
  cv::Mat threshold_image;
  cv::threshold(grayscaled_image, threshold_image, 150, 255, cv::THRESH_BINARY);

  cv::waitKey(0);
  cv::imwrite("./assets/threshold_image.jpg", threshold_image);
  cv::destroyAllWindows(); 

  // 3) find contours with CHAIN_APPROX_NONE and CHAIN_APPROX_SIMPLE 
  vector<vector<cv::Point>> contours;
  vector<cv::Vec4i> hierarchy; 
  /* cv::findContours(threshold_image, contours, hierarchy, cv::RETR_TREE, cv::CHAIN_APPROX_NONE); */
  cv::findContours(threshold_image, contours, hierarchy, cv::RETR_TREE, cv::CHAIN_APPROX_SIMPLE);
   
  // 4) draw contours on original rgb image
  cv::Mat image_copy = image.clone();
  cv::drawContours(image_copy, contours, -1, cv::Scalar(0, 255, 0), 2);

  cv::imshow("simple approximation: ", image_copy);
  cv::waitKey(0);
  cv::imwrite("./assets/contours_simple.jpg", image_copy);
  cv::destroyAllWindows(); 

  return 0;
}
