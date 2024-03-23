import { createFileRoute } from '@tanstack/react-router'
import PageContent from '../../components/PageContent'
import { UploadOutlined } from '@ant-design/icons';
import { Form, Input, Button, FormProps, Radio, Select, Upload, message, Space } from 'antd'
import { useEffect, useState } from 'react';
import axios from 'axios';

const cutImageData = (img: string, callback: { (cutImage: string): void; }) => {
  var image = new Image();
  image.onload = function () {
      var canvas = document.createElement('canvas');

      var standard_w = 480;
      var standard_h = 640;

      canvas.width = standard_w;
      canvas.height = standard_h;

      var ctx = canvas.getContext('2d') as CanvasRenderingContext2D;
      //以下代码抄自 http://blog.csdn.net/vivian_jay/article/details/68933161
      //谢谢 CSDN 用户 少女心の程序媛 的耐心推导

      // 裁剪图片中间部分
      if (image.width > standard_w && image.height > standard_h || image.width < standard_w && image.height < standard_h) {
          if (image.height * standard_w > image.width * standard_h) {
              ctx.drawImage(image, 0, (image.height - standard_h * image.width / standard_w) / 2, image.width, standard_h * image.width / standard_w, 0, 0, standard_w, standard_h)
          } else {
              ctx.drawImage(image, (image.width - standard_w * image.height / standard_h) / 2, 0, standard_w * image.height / standard_h, image.height, 0, 0, standard_w, standard_h)
          }
      }
      // 拉伸图片
      else {
          if (image.width < standard_w) {
              ctx.drawImage(image, 0, (image.height - standard_h * image.width / standard_w) / 2, image.width, standard_h * image.width / standard_w, 0, 0, standard_w, standard_h)
          } else {
              ctx.drawImage(image, (image.width - standard_w * image.height / standard_h) / 2, 0, standard_w * image.height / standard_h, image.height, 0, 0, standard_w, standard_h)
          }
      }
      var dataURL = canvas.toDataURL('image/jpeg');
      callback(dataURL);
  };
  image.src = img;
}

const onFinish = (value: any) => {
  console.log(value)
  axios.post('/api/student/info/set', value)
  .then(response => {
    alert(JSON.stringify(response.data))
    window.location.href = "/reg/service-hall"
  })
  .catch((error: any) => {
    alert(JSON.stringify(error.response.data))
  })
}

const onFinishFailed: FormProps["onFinishFailed"] = (errorInfo) => {
  console.log('Failed:', errorInfo);
  alert(errorInfo.errorFields[0].errors[0]);
};

export const Route = createFileRoute('/reg/basic-info')({
  loader: async (params : any) => {
    params = params.location.search;
    console.log(params)
    let uid = params.uid;
    if (!uid) {
      const response = await axios.get('/api/whoami');
      uid = response.data.uid;
    }
    const response = await axios.get('/api/student/info/get', {params: {uid: uid}});
    return Object.assign({uid: uid}, response.data)
  },
  component: () => {
    const [form] = Form.useForm();
    const [imageData, setImageData] = useState<string>();
    const loader_data = Route.useLoaderData();
    useEffect(() => {
      setImageData(loader_data.photo)
    }, [])

    return (
      <>
      <PageContent>
        
        <h1> 报名 · 第二步</h1>
        <Form
          name="basic"
          labelCol={{ span: 8 }}
          wrapperCol={{ span: 16 }}
          style={{ maxWidth: 600 }}
          layout="horizontal"
          variant="filled"
          initialValues={loader_data}
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
          autoComplete="off"
          form={form}
        >
          <h2> 基本信息 </h2>
          <Form.Item
            label="学号"
            name="uid"
          >
            <Input disabled/>
          </Form.Item>
          <Form.Item
            label="姓名"
            name="name"
            help="如有学籍姓名与证件姓名不一致的情况，请及时联系管理员"
          >
            <Input maxLength={20} />
          </Form.Item>
          <Form.Item
            label="性别"
            name="gender"
            // rules={[{ required: true }]}
            help="证件上显示的性别"
          >
            <Radio.Group
            options={[
              {
                value: 0,
                label: "男"
              },
              {
                value: 1,
                label: "女"
              }
            ]}/>
          </Form.Item>

          <Form.Item 
            label="校区"
            name="campus"
            // rules={[{ required: true }]}
          >
            <Select
              options={[
                {
                  value: 1,
                  label: "中心校区"
                }
              ]}/>
          </Form.Item>

          <Form.Item 
            label="标准证件照"
            >
              <Upload 
                maxCount={1}
                onRemove= {() => {
                  setImageData("");
                  form.setFieldsValue({ photo: undefined });
                }}
                beforeUpload={(file) => {
                  const isJpgOrPng = file.type === 'image/jpeg' || file.type === 'image/png';
                  if (!isJpgOrPng) {
                    message.error('You can only upload JPG/PNG file!');
                    return false;
                  }
                  const reader = new FileReader();
                  reader.addEventListener("load", () => {
                    cutImageData(reader.result as string, (cutImage: string) => {
                      setImageData(cutImage);
                      form.setFieldsValue({ photo: cutImage });
                    })
                  })
                  reader.readAsDataURL(file);
                  return false;
                }}
              >
                <Button icon={<UploadOutlined />}>Select File</Button>
              </Upload>
              {imageData ? <img src={imageData} width="50%"></img>: null}
          </Form.Item>
          <Form.Item label="证件照" name="photo" hidden
          >
            <Input value={imageData}></Input>
          </Form.Item>
          

          <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
            <Space>
              {/* <Button>验证表单</Button> */}
              <Button type="primary" htmlType="submit">
                下一步
              </Button>
            </Space>
          </Form.Item>
        </Form>
      </PageContent>
      </>
    )
  },
})
