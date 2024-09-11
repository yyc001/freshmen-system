import React, { useEffect, useState } from 'react';
import { Form, Input, Select, Button, Radio, Space } from 'antd';
import Title from 'antd/es/typography/Title';
import ImageUploader from './ImageUploader';
type FormField = {
    name: string;
    label: string;
    help?: string;
    type: 'title' | 'text' | 'radio' | 'select' | 'profile' | 'dtext';  // 根据后端定义的字段类型
    options?: { label: string; value: string }[];
    pattern?: string;
    optional? : boolean;
    split?: string;
    childnames?: string[];
};
  
interface DynamicFormProps {
    getFields: (setFields: any) => void;
    onFinish: (values: any) => void;
    initialValues: any;
    children: any;
}

const DynamicForm: React.FC<DynamicFormProps> = ({getFields, onFinish, initialValues, children}) => {
  const [fields, setFields] = useState<FormField[]>([]);
  const [form] = Form.useForm();

  useEffect(() => {
    getFields(setFields);
    // console.log(fields);
  }, []);

  // 根据字段类型渲染表单项
  const renderFormItem = (field: FormField) => {
    switch (field.type) {
    case 'title':
        return (<Title level={3}>{field.label}</Title>);
    case 'text':
        return (
            <Form.Item 
                key={field.name} name={field.name} 
                label={field.label}
                help={field.help}
                rules={[{ required: !field.optional }]}
            >
                <Input pattern={field.pattern}/>
            </Form.Item>
        );
    case 'radio':
        return (
            <Form.Item 
                key={field.name} name={field.name} 
                label={field.label}
                help={field.help}
                rules={[{ required: !field.optional }]}
            >
                <Radio.Group options={field.options}/>
            </Form.Item>
        );
    case 'select':
        return (
            <Form.Item 
                key={field.name} name={field.name} 
                label={field.label}
                help={field.help}
                rules={[{ required: !field.optional }]}
            >
                <Select options={field.options}/>
            </Form.Item>
        );
    case 'profile':
        return (
            <Form.Item 
                key={field.name} name={field.name} 
                label={field.label}
                help={field.help}
                rules={[{ required: !field.optional }]}
            >
                <ImageUploader />
            </Form.Item>
        );
    case 'dtext':
        return (
            <Form.Item 
                label={field.label}
            >
            <Space.Compact>
                <Form.Item 
                    name={field.childnames ? field.childnames[0]: undefined}
                    rules={[{ required: !field.optional }]}
                    help={field.help}
                >
                    <Input addonAfter={field.split}/>
                </Form.Item>
                <Form.Item 
                    name={field.childnames ? field.childnames[1]: undefined}
                    rules={[{ required: !field.optional }]}
                >
                    <Input />
                </Form.Item>
            </Space.Compact>
            </Form.Item>
        );
    default:
        return null;
    }
  };

  return (
    <Form           
        // name="basic"
        labelCol={{ span: 8 }}
        // wrapperCol={{ span: 16 }}
        style={{ maxWidth: 800 }}
        layout="horizontal"
        variant="filled"
        initialValues={initialValues}
        onFinish={onFinish}
        // onFinishFailed={onFinishFailed}
        // autoComplete="off"
        form={form}
    >
      {fields.map((field) => (
          renderFormItem(field)
      ))}
      {children}
      <Form.Item>
        <Button type="primary" htmlType="submit">
          提交
        </Button>
      </Form.Item>
    </Form>
  );
};

export default DynamicForm;
