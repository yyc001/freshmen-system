import { createFileRoute } from '@tanstack/react-router'
import PageContent from '../../components/PageContent'
import { Button, Form, Input, Space } from 'antd'
import { useEffect } from 'react'
import axios from 'axios'

export const Route = createFileRoute('/reg/contact-details')({
  loader: async (params : any) => {
    params = params.location.search;
    console.log(params)
    let uid = params.uid;
    if (!uid) {
      const response = await axios.get('/api/whoami');
      uid = response.data.uid;
    }
    const response = await axios.get('/api/student/info/get', {params: {uid: uid}});
    return {
      params: { uid: uid},
      data: response.data
    };
  },
  component: () => {
    const loader_data = Route.useLoaderData();
    // console.log(loader_data);
    const [form] = Form.useForm();
    const getOTP = async () => {
      const response = await axios.get('/api/student/otp');
      // TODO backend implement otp
      console.log(response.data)
    }
    const onFinish = (value: any) => {
      console.log(value)
      axios.post('/api/student/info/set', value)
      .then(response => {
        alert(JSON.stringify(response.data))
        window.location.href = "/reg/basic-info"
      })
      .catch((error: any) => {
        alert(JSON.stringify(error.response.data))
      })
    }
    useEffect(() => {
    }, []);
    return (
      <>
    <PageContent>
        <h1> 第一步 · 绑定手机 </h1>
        <Form
          name="basic"
          form={form}
          labelCol={{ span: 8 }}
          wrapperCol={{ span: 16 }}
          style={{ maxWidth: 600 }}
          layout="horizontal"
          variant="filled"
          // initialValues={getInitialValues()}
          autoComplete="off"
          onFinish={onFinish}
        >
          <h2> 基本信息 </h2>
          <Form.Item hidden name="uid" initialValue={loader_data.params.uid}/>
          <Form.Item
            label="手机号"
            name="tel"
            help="仅支持 +86 号码"
            rules={[{ required: true }]}
          >
            <Space.Compact style={{ width: '100%' }}>
                <Input type="tel" pattern='\d{7,15}' width="auto" maxLength={15} defaultValue={loader_data.data.tel}/> 
                <Button onClick={getOTP}>获取验证码</Button>
            </Space.Compact>
                
          </Form.Item>
          <Form.Item
            label="短信验证码"
            name="otp"
            rules={[{ required: true , message: '请填写验证码'}]}
          >
            <Input maxLength={20}/>
          </Form.Item>
          <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
            <Space>
                <Button type="primary" htmlType="submit">下一步</Button>
            </Space>
          </Form.Item>
        </Form>
      </PageContent>
      </>
    )
  },
})