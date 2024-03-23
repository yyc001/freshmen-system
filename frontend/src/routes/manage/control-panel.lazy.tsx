import { createLazyFileRoute } from '@tanstack/react-router'
import PageContent from '../../components/PageContent'
import { Button, DatePicker, Form, Radio } from 'antd'
import axios from 'axios';
import { useEffect } from 'react';
import dayjs from 'dayjs';

export const Route = createLazyFileRoute('/manage/control-panel')({
  component: () => {
    const [form] = Form.useForm();
    function onFinish(value: any) {
      axios.post('/api/global/set', {
        'start-time': value.time[0],
        'end-time': value.time[1],
        'entrance': value.entrance
      }).then((res) => {
        alert(JSON.stringify(res.data));
      })
    }
    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await axios.get('/api/global/get');
          form.setFieldsValue({
            time: [dayjs(response.data.start_time), dayjs(response.data.end_time)],
            entrance: response.data.entrance
          })
        } catch (error) {
          console.error('Fetching initial data failed:', error);
        }
      };
      fetchData();
    }, []);
  
    return (
      <>
        <PageContent>
          <h1> 学生管理 </h1>
          <Form
            name="basic"
            labelCol={{ span: 8 }}
            wrapperCol={{ span: 16 }}
            style={{ maxWidth: 600 }}
            layout="horizontal"
            variant="filled"
            onFinish={onFinish}
            form={form}
            >
            <Form.Item
                label="报名时间"
                name="time"
            >
                <DatePicker.RangePicker showTime
                />
            </Form.Item>
            <Form.Item
                label="报名通道"
                name="entrance"
            >
                <Radio.Group
                    options={[
                        {
                            label: '开启',
                            value: 'open'
                        },
                        {
                            label: '关闭',
                            value: 'close'
                        }
                    ]}
                    />
            </Form.Item>
            <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
                <Button type="primary" htmlType="submit">保存</Button>
          </Form.Item>
          </Form>
        </PageContent> 
      </>
    )
  },
})