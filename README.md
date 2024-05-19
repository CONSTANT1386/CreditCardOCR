- ## [Source: 迪哥谈AI](https://www.bilibili.com/video/BV1jc411s7gN?p=16)
- ### Display:
  - **Original picture**

    ![original picture](assets/credit_card.png)
   - **contour picture**
     
    ![contour](assets/contour.png)
    - **result picture**
      
    ![result](assets/result.png)

- ### Procedure:
    - #### get template for each digit 
    - #### get the contour for the region to be matched
      - the each digit with the same size of the digit template
      - to get the contour of digit region on the card, we can do these steps：
      1. tophat -- which highlight the brighter part e.g. digit\pattern\letter etc.
      2. sobel gradient -- to remain and enforce the edge information
      3. MORPH_CLOSE -- morphological close operation (first dilate then erode), blending the remaining region togather
      4. THRESH_OTSU -- find the suitable threshold automatically, and make it binary, waiting for finding the contour
