import React, { useEffect, useState } from 'react';

interface ImageUploaderProps {
  value?: string;
  onChange?: (value: string) => void;
  width?: number; // 期望的宽度
  height?: number; // 期望的高度
  displayStyle?: {width: string, height: string}
}

const ImageUploader: React.FC<ImageUploaderProps> = ({
      value, 
      onChange, 
      width = 358, 
      height = 441,
      displayStyle = {width: '150px'} 
    }) => {
  const [previewImage, setPreviewImage] = useState<string | null>(null);

  // 当表单的 initialValues 中的 value 发生变化时，设置预览图片
  useEffect(() => {
    if (value) {
      setPreviewImage(value);
    }
  }, [value]);

  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const reader = new FileReader();

      reader.onload = () => {
        const img = new Image();
        img.src = reader.result as string;

        img.onload = () => {
          const canvas = document.createElement('canvas');
          const ctx = canvas.getContext('2d');
          if (!ctx) return;

          // 设置 canvas 的宽高为目标裁切大小
          canvas.width = width;
          canvas.height = height;

          // 计算图片裁切位置，确保居中裁切
          const aspectRatio = img.width / img.height;
          const targetAspectRatio = width / height;

          let sx = 0, sy = 0, sw = img.width, sh = img.height;

          if (aspectRatio > targetAspectRatio) {
            // 图片过宽，裁切宽度
            sw = img.height * targetAspectRatio;
            sx = (img.width - sw) / 2;
          } else {
            // 图片过高，裁切高度
            sh = img.width / targetAspectRatio;
            sy = (img.height - sh) / 2;
          }

          // 将裁切的图片绘制到 canvas 上
          ctx.drawImage(img, sx, sy, sw, sh, 0, 0, width, height);

          // 将 canvas 内容转换为 Base64 编码
          const base64Image = canvas.toDataURL('image/jpeg');
          
          // 调用 onChange 传递 Base64 编码
          onChange?.(base64Image);
          setPreviewImage(base64Image); // 设置预览图片
        };
      };

      reader.readAsDataURL(file); // 读取文件
    }
  };

  return (
    <div>
      {/* 文件上传输入框 */}
      <input type="file" accept="image/*" onChange={handleImageChange} />
      
      {/* 图片预览 */}
      {previewImage && (
          <img src={previewImage} alt="Preview" style={displayStyle} />
      )}
    </div>
  );
};

export default ImageUploader;
