import React from "react";
import { Layout, Menu, theme } from 'antd';
import Link from "antd/es/typography/Link";
import { useRouterState } from "@tanstack/react-router";
import Cookies from 'js-cookie';

const { Header, Content, Footer } = Layout;

interface PageContentProps {
    identity?: number[]
    children?: React.ReactNode
}

const PageContent: React.FC<PageContentProps> = ({children}) => {
    const isStudent = Cookies.get('student') ?? 0;
    const isAdmin = Cookies.get('admin') ?? 0;
    const isInterviewer = Cookies.get('interviewer') ?? 0;
    const {
        token: { colorBgContainer, borderRadiusLG },
      } = theme.useToken();
    
    return (
        <>
        <Layout>
        <Header style={{ display: 'flex', alignItems: 'center' }}>
            <div>
                <span style={{color:'white', marginRight: 30}}><b>报名系统</b></span>
            </div>
            <Menu
                theme="dark"
                mode="horizontal"
                defaultSelectedKeys={[useRouterState().location.pathname]}
                style={{ flex: 1, minWidth: 0 }}
                items={[
                    {
                        key: "/",
                        label: <Link href="/"> 首页 </Link>
                    },
                    {
                        key: "/help",
                        label: <Link href="/help"> 帮助 </Link>
                    }].concat(isStudent ? [
                    {
                        key: "/reg/contact-details",
                        label: <Link href="/reg/contact-details"> 报名 · 第一步 </Link>

                    },
                    {
                        key: "/reg/basic-info",
                        label: <Link href="/reg/basic-info"> 报名 · 第二步 </Link>
                    },
                    {
                        key: "/reg/service-hall",
                        label: <Link href="/reg/service-hall"> 报名 · 第三步 </Link>
                    },
                    {
                        key: "/reg/attachments",
                        label: <Link href="/reg/attachments"> 报名 · 第四步 </Link>
                    },
                    {
                        key: "/reg/ready-submit",
                        label: <Link href="/reg/ready-submit"> 报名 · 第五步 </Link>
                    }] : []).concat(isAdmin ? [
                    {
                        key: "/manage/submissions",
                        label: <Link href="/manage/submissions"> 学生管理 </Link>
                    },
                    {
                        key: "/manage/control-panel",
                        label: <Link href="/manage/control-panel"> 控制面板 </Link>
                    },
                ] : [])}
            />
        </Header>
        <Content style={{ padding: '20px 48px' }}>
            <div
            style={{
                background: colorBgContainer,
                minHeight: 280,
                padding: 24,
                borderRadius: borderRadiusLG,
                // maxWidth: 800,
                margin: "auto"
            }}
            >
            {children}
            </div>
        </Content>
        <Footer style={{ textAlign: 'center' }}>
            Ant Design ©{new Date().getFullYear()} Created by Ant UED
        </Footer>
        </Layout>
        </>
    );
};

export default PageContent;